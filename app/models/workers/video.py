import sys
import time
import logging
import cv2
import numpy as np
import torch
import multiprocessing as mp
from collections import deque, defaultdict
from PyQt5 import QtCore, QtGui
from ultralytics import YOLO

class VideoCaptureWorker(QtCore.QThread):
    frameCaptured = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, camera_index=0, resolution=(640, 480), target_fps=30, parent=None):
        super().__init__(parent)
        self.camera_index = camera_index
        self.resolution = resolution
        self.target_fps = target_fps
        self._running = False
        self.frame_times = deque(maxlen=10)

    # VideoCaptureWorker sınıfındaki run metodunu güncelleyin:
    def run(self):
        self._running = True
        cap = cv2.VideoCapture(self.camera_index)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
        if not cap.isOpened():
            logging.error(f"Unable to open camera index {self.camera_index}")
            return

        while self._running:
            start_time = time.perf_counter()
            ret, frame = cap.read()
            if ret:
                # Flip işlemi KALDIRILDI
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Orijinal frame
                height, width, channels = rgb_frame.shape
                bytes_per_line = channels * width
                qimg = QtGui.QImage(rgb_frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
                self.frameCaptured.emit(qimg.copy())
            else:
                logging.warning("Failed to read frame from camera.")
                continue
            elapsed = time.perf_counter() - start_time
            self.frame_times.append(elapsed)
            sleep_time = max((1.0 / self.target_fps) - elapsed, 0)
            time.sleep(sleep_time)
        cap.release()

    def stop(self):
        self._running = False
        self.wait()

def yolo_worker(input_queue, output_queue):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"YOLO worker using device: {device}")

    model = YOLO("yolov8n.pt").to(device)
    model.fuse()
    track_history = defaultdict(lambda: [])

    try:
        while True:
            try:
                frame = input_queue.get(timeout=1)
                if frame is None:
                    break

                with torch.inference_mode():
                    results = model.track(
                        frame,
                        persist=True,
                        classes=[0],
                        device=device,
                        half=True if device == 'cuda' else False,
                        verbose=False
                    )

                if results and results[0].boxes and results[0].boxes.id is not None:
                    boxes = results[0].boxes.xywh.cpu().numpy()
                else:
                    boxes = []

                annotated_frame = results[0].plot() if results else frame
                output_queue.put((annotated_frame, boxes))

            except mp.queues.Empty:
                if sys.is_finalizing():
                    break

    except Exception as e:
        print(f"YOLO worker exception: {e}")
    finally:
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        model = None
        print("YOLO worker shutting down")

class YOLOVideoWorker(QtCore.QThread):
    frameCaptured = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, camera_index=0, target_fps=30, resolution=(640, 480), parent=None):
        super().__init__(parent)
        self.camera_index = camera_index  # Seçilen kamera indeksi
        self.target_fps = target_fps
        self.resolution = resolution
        self._running = False
        self.last_boxes = []  # Eklenen attribute

        ctx = mp.get_context('spawn')
        self.input_queue = ctx.Queue(maxsize=1)
        self.output_queue = ctx.Queue(maxsize=1)
        self.yolo_process = ctx.Process(
            target=yolo_worker,
            args=(self.input_queue, self.output_queue),
            daemon=True
        )
        self.yolo_process.start()

    def run(self):
        self._running = True
        # Seçilen kamera indeksini kullanıyoruz:
        cap = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)
        if not cap.isOpened():
            print(f"Kamera {self.camera_index} açılamadı, alternatif video dosyası deneniyor.")
            # Alternatif olarak bir video dosyasını deneyebilirsiniz veya direkt return yapabilirsiniz.
            cap = cv2.VideoCapture("document_5893026422414382415.mp4")
            if not cap.isOpened():
                print(f"Error: Video kaynağı açılamadı (kamera {self.camera_index}).")
                return

        last_annotated_frame = None

        try:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
            cap.set(cv2.CAP_PROP_FPS, self.target_fps)
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

            while self._running:
                start_time = time.perf_counter()
                ret, frame = cap.read()
                if not ret:
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue

                try:
                    if self.input_queue.empty():
                        self.input_queue.put(frame, block=False)
                except Exception:
                    pass

                try:
                    annotated_frame, boxes = self.output_queue.get_nowait()
                    last_annotated_frame = annotated_frame
                    if isinstance(boxes, np.ndarray):
                        self.last_boxes = boxes.tolist()
                    else:
                        self.last_boxes = boxes
                except Exception:
                    annotated_frame = last_annotated_frame if last_annotated_frame is not None else frame

                self._emit_frame(annotated_frame)

                elapsed = time.perf_counter() - start_time
                sleep_time = max((1.0 / self.target_fps) - elapsed, 0)
                time.sleep(sleep_time)

        finally:
            cap.release()
            self._cleanup_processes()

    def _emit_frame(self, frame):
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qimg = QtGui.QImage(frame.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.frameCaptured.emit(qimg.copy())

    def stop(self):
        self._running = False
        if self.isRunning():
            if not self.wait(2000):  # wait süresini artırıyoruz
                logging.warning("Thread did not finish in time, terminating forcefully.")
                self.terminate()  # Zorla sonlandırma
                self.wait(1000)
        self._cleanup_processes()

    def _cleanup_processes(self):
        try:
            while not self.input_queue.empty():
                self.input_queue.get_nowait()
            self.input_queue.put(None, timeout=0.5)
        except Exception:
            pass

        if self.yolo_process.is_alive():
            self.yolo_process.terminate()
            self.yolo_process.join(timeout=1)
            if self.yolo_process.exitcode is None:
                self.yolo_process.kill()

        self.input_queue.close()
        self.output_queue.close()
        print("All resources cleaned up")