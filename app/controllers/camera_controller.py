import logging
import multiprocessing
from PyQt5 import QtCore, QtGui
from app.models.workers.video import YOLOVideoWorker  # YOLOVideoWorker importu

class CameraController:
    def __init__(self, parent):
        self.parent = parent
        self.video_worker = None
        self.yolo_initialized = False
        self._init_yolo_model()
        self.model_check_timer = QtCore.QTimer(self.parent)
        self.model_check_timer.timeout.connect(self._check_model_ready)
        self.model_check_timer.start(300)

    def _init_yolo_model(self):
        """Modeli arka planda sessizce yükler"""
        ctx = multiprocessing.get_context('spawn')
        self.parent.yolo_process = ctx.Process(
            target=self.parent._background_model_init,
            daemon=True
        )
        self.parent.yolo_process.start()

    def _check_model_ready(self):
        if not self.parent.yolo_process.is_alive():
            self.yolo_initialized = True
            self.model_check_timer.stop()
            self.parent.ui.openCamera_pushButton.setEnabled(True)  # Butonu aktif et
            logging.info("Model ready - Camera button enabled")

    def open_camera(self):
        if not self.yolo_initialized:
            logging.warning("Camera open attempted before model initialization!")
            return
        cam_index = self.parent.ui.videoCapture_comboBox.currentData()
        if cam_index is None or cam_index == -1:
            logging.error("Geçerli bir kamera seçilmedi!")
            return
        if self.video_worker is not None:
            self.close_camera()
        self.parent.show_loading_gif()
        resolution = self.parent.ui.resolution_comboBox.currentText().split('x')
        target_res = (int(resolution[0]), int(resolution[1])) if len(resolution) == 2 else (640, 480)
        self.video_worker = YOLOVideoWorker(
            camera_index=cam_index,
            target_fps=30,
            resolution=target_res
        )
        self.video_worker.frameCaptured.connect(self.update_camera_image)
        self.video_worker.start()
        logging.info(f"Kamera {cam_index} ile açıldı.")
        self.parent.ui.openCamera_pushButton.setEnabled(False)
        self.parent.ui.closeCamera_pushButton.setEnabled(True)

    def close_camera(self):
        if self.video_worker is not None:
            try:
                self.video_worker.frameCaptured.disconnect(self.update_camera_image)
            except Exception as e:
                logging.warning(f"Signal disconnect failed: {e}")

            self.video_worker.stop()
            self.video_worker = None
            self.parent.ui.cameraShown_label.clear()
            logging.info("Camera closed.")
            self.parent.snap_session_folder = None
            self.parent.snap_threadpool.waitForDone(3000)
            self.parent.ui.openCamera_pushButton.setEnabled(True)
            self.parent.ui.closeCamera_pushButton.setEnabled(False)
            self.parent.ui.closeCamera_pushButton.setStyleSheet("background-color: #F44336; color: white;")
            self.parent.ui.openCamera_pushButton.setStyleSheet("")

    def update_camera_image(self, qimg):
        pixmap = QtGui.QPixmap.fromImage(qimg)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(
                self.parent.ui.cameraShown_label.size(),
                QtCore.Qt.KeepAspectRatioByExpanding,
                QtCore.Qt.SmoothTransformation
            )
            self.parent.ui.cameraShown_label.setPixmap(scaled_pixmap)
        with QtCore.QMutexLocker(self.parent.frame_lock):
            self.parent.current_frame = qimg.copy() if not qimg.isNull() else None

    def process_click(self, pos):
        if self.parent.current_frame is None or self.video_worker is None:
            return
        label_size = self.parent.ui.cameraShown_label.size()
        img_width = self.parent.current_frame.width()
        img_height = self.parent.current_frame.height()
        ratio_x = img_width / label_size.width()
        ratio_y = img_height / label_size.height()
        orig_x = pos.x() * ratio_x
        orig_y = pos.y() * ratio_y
        if hasattr(self.video_worker, "last_boxes") and self.video_worker.last_boxes:
            for box in self.video_worker.last_boxes:
                x_center, y_center, w, h = box
                x_min = x_center - (w / 2)
                y_min = y_center - (h / 2)
                if (x_min <= orig_x <= x_min + w) and (y_min <= orig_y <= y_min + h):
                    x = int(max(0, x_min))
                    y = int(max(0, y_min))
                    w_int = int(min(w, img_width - x))
                    h_int = int(min(h, img_height - y))
                    with QtCore.QMutexLocker(self.parent.frame_lock):
                        cropped = self.parent.current_frame.copy(x, y, w_int, h_int)
                    pix = QtGui.QPixmap.fromImage(cropped)
                    target_size = self.parent.ui.bodyDetectedShown_label.size()
                    scaled_pix = pix.scaled(target_size, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
                    self.parent.ui.bodyDetectedShown_label.setPixmap(scaled_pix)
                    logging.info("Bounding box seçildi ve etikete tam oturacak şekilde ölçeklendi.")
                    break