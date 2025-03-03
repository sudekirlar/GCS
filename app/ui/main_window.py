import sys
import os
import json
import logging
import cv2
import numpy as np
import torch
import serial.tools.list_ports
import multiprocessing
from datetime import datetime
from collections import deque
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings  # Sadece ihtiyacınız olan sınıfı import edin
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtWebChannel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import pyqtSignal, QObject, QMetaObject, QRunnable, Qt
from ultralytics import YOLO
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Proje içi importlar
from app.ui.resources import res  # QT Designer .ui dosyasından üretilen res.py
from app.controllers.drone_controller import DroneController
from app.controllers.camera_controller import CameraController
from app.controllers.map_controller import MapController
from app.controllers.snapshot_controller import SnapshotController
from app.services.drone_data import DroneDataManager
from app.services.bridge import Bridge
from app.utils.logging.handlers import CriticalTextEditHandler
from app.utils.logging.manager import LogManager
from app.models.workers.video import YOLOVideoWorker

# UI_class.py QT Designer tarafından oluşturulmuş olmalı
from app.ui.resources.UI_class import Ui_Form

current_dir = os.path.dirname(os.path.abspath(__file__))
# Eğer main_window.py "app/ui" içinde ise ve logging.conf "app/utils/logging" altında yer alıyorsa:
config_file = os.path.join(current_dir, "..", "utils", "logging", "logging.conf")
LogManager.setup_logging(config_file)

# Buraya dikkat.
map_path = os.path.abspath(os.path.join("app", "ui", "views", "map.html"))

class SerialMonitor(QtWidgets.QWidget):
    @QtCore.pyqtSlot()
    def resetSnapInProgress(self):
        self.snapshot_controller.resetSnapInProgress()

    def show_loading_gif(self):
        # main_window.py "app/ui" içinde olduğu için proje kök dizinine iki seviye yukarı çıkıyoruz
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        # Dosyanın tam yolunu oluşturuyoruz
        gif_path = os.path.join(base_dir, "app", "assets", "icons", "camera_shutter.gif")

        self.movie = QMovie(gif_path)
        self.movie.setScaledSize(self.ui.cameraShown_label.size())
        self.ui.cameraShown_label.setMovie(self.movie)
        self.movie.start()

    def hide_loading_gif(self):
        if hasattr(self, 'movie'):
            self.movie.stop()

    def __init__(self):
        super().__init__()
        self.channel = None
        self.bridge = None
        self.webView = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        critical_handler = CriticalTextEditHandler(self.ui.criticalShown_textEdit)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        critical_handler.setFormatter(formatter)
        logging.getLogger().addHandler(critical_handler)

        self.lock = QtCore.QMutex()
        self.threadpool = QtCore.QThreadPool()
        self.processed_data_count = 0
        self.received_data_count = 0

        self.field_map = {
            "Yaw": self.ui.yaw_textEdit,
            "Roll": self.ui.roll_textEdit,
            "Pitch": self.ui.pitch_textEdit,
            "Latitude": self.ui.latitude_textEdit,
            "Longitude": self.ui.longitude_textEdit,
            "Altitude": self.ui.altitude_textEdit,
            "Speed": self.ui.speed_textEdit,
            "HDOP": self.ui.hdop_textEdit,
            "currentMode": self.ui.currentMode_textEdit,
        }
        self.latestData = {
            "Latitude": None,
            "Longitude": None,
            "Yaw": None,
            "Speed": None,
            "HDOP": None,
        }

        self.routePoints = []
        self.mapReady = False

        # UI bağlantıları (Controller'lara delege edilecek)
        self.ui.openTelemetry_pushButton.clicked.connect(lambda: self.drone_controller.open_port())
        self.ui.closeTelemetry_pushButton.clicked.connect(lambda: self.drone_controller.close_port())
        self.ui.addMarker_pushButton.clicked.connect(lambda: self.map_controller.add_marker())
        self.ui.clearMarker_pushButton.clicked.connect(lambda: self.map_controller.clear_markers())
        self.ui.openCamera_pushButton.clicked.connect(lambda: self.camera_controller.open_camera())
        self.ui.closeCamera_pushButton.clicked.connect(lambda: self.camera_controller.close_camera())
        self.ui.snapshoot_pushButton.clicked.connect(lambda: self.snapshot_controller.snapshoot())
        self.ui.goToFocus_pushButton.clicked.connect(lambda: self.map_controller.go_to_focus())
        self.ui.clearPath_pushButton.clicked.connect(lambda: self.map_controller.clear_path())
        self.list_available_ports()
        self.list_available_cameras()
        self.ui.videoCapture_comboBox.currentIndexChanged.connect(self.update_resolution_options)
        self.populate_default_resolutions()

        # Yeni Controller nesnelerinin oluşturulması
        self.drone_controller = DroneController(self)
        self.camera_controller = CameraController(self)
        self.map_controller = MapController(self)
        self.snapshot_controller = SnapshotController(self)



        self.video_worker = None
        self.current_frame = None
        self.frame_lock = QtCore.QMutex()
        self.snap_base_dir = r"C:\Users\SUDE\Desktop\birinci taslak 190225\Snapshoots"
        self.snap_session_folder = None
        self.snap_threadpool = QtCore.QThreadPool()
        self.snap_in_progress = False

        self.ui.openCamera_pushButton.setEnabled(True)
        self.ui.closeCamera_pushButton.setEnabled(False)
        self.ui.openCamera_pushButton.setStyleSheet("")
        self.ui.closeCamera_pushButton.setStyleSheet("")

        self.droneWorker = None

        # Drone komut buton bağlantıları (Controller üzerinden)
        self.ui.changeMode_pushButton.clicked.connect(lambda: self.drone_controller.on_change_mode_clicked())
        self.ui.arm_pushButton.clicked.connect(lambda: self.drone_controller.on_arm_clicked())
        self.ui.disarm_pushButton.clicked.connect(lambda: self.drone_controller.on_disarm_clicked())
        self.ui.takeOff_pushButton.clicked.connect(lambda: self.drone_controller.on_takeoff_clicked())
        self.ui.land_pushButton.clicked.connect(lambda: self.drone_controller.on_land_clicked())

        self.modeTimer = QtCore.QTimer(self)
        self.modeTimer.timeout.connect(lambda: self.drone_controller.update_current_mode())
        self.modeTimer.start(5000)

        self.ui.cameraShown_label.installEventFilter(self)

        self.yolo_initialized = False
        self.yolo_process = None
        self._init_yolo_model()

        self.ui.openCamera_pushButton.setEnabled(False)

        self.battery_worker = None
        self.battery_thread = None

        self.webView = QWebEngineView(self)
        self.init_map_view()

    def _init_yolo_model(self):
        """Modeli arka planda sessizce yükler"""
        ctx = multiprocessing.get_context('spawn')
        self.yolo_process = ctx.Process(
            target=self._background_model_init,
            daemon=True
        )
        self.yolo_process.start()
        self.model_check_timer = QtCore.QTimer(self)
        self.model_check_timer.timeout.connect(self._check_model_ready)
        self.model_check_timer.start(300)

    @staticmethod
    def _background_model_init():
        try:
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
            model = YOLO("yolov8n.pt").to(device)
            for _ in range(5):
                dummy_frame = np.random.randint(0, 255, (640, 480, 3), dtype=np.uint8)
                model.predict(dummy_frame, verbose=False)
            logging.info("[BACKGROUND] YOLO model initialized")
        except Exception as e:
            logging.error(f"[BACKGROUND] Model init error: {str(e)}")

    def _check_model_ready(self):
        if not self.yolo_process.is_alive():
            self.yolo_initialized = True
            self.model_check_timer.stop()
            self.ui.openCamera_pushButton.setEnabled(True)
            logging.info("Model ready - Camera button enabled")

    def update_resolution_options(self):
        cam_index = self.ui.videoCapture_comboBox.currentData()
        candidate_resolutions = [(640, 480), (800, 600), (1280, 720), (1920, 1080)]
        valid_resolutions = []
        if cam_index is None or cam_index == -1:
            self.ui.resolution_comboBox.clear()
            self.ui.resolution_comboBox.addItem("No Resolution")
            return
        cap = cv2.VideoCapture(cam_index)
        if not cap.isOpened():
            logging.error(f"Unable to open camera index {cam_index} for resolution test.")
            self.ui.resolution_comboBox.clear()
            self.ui.resolution_comboBox.addItem("No Resolution")
            return
        for (w, h) in candidate_resolutions:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
            actual_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            actual_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            if abs(actual_w - w) < 50 and abs(actual_h - h) < 50:
                valid_resolutions.append(f"{w}x{h}")
        cap.release()
        self.ui.resolution_comboBox.clear()
        if valid_resolutions:
            self.ui.resolution_comboBox.addItems(valid_resolutions)
        else:
            self.ui.resolution_comboBox.addItem("640x480")

    def list_available_ports(self):
        self.ui.comPortTelemetry_comboBox.clear()
        available_ports = [port.device for port in serial.tools.list_ports.comports()]
        available_ports.append("TCP:127.0.0.1:5760")
        if available_ports:
            self.ui.comPortTelemetry_comboBox.addItems(available_ports)
        else:
            self.ui.comPortTelemetry_comboBox.addItem("No Ports Available")

    def list_available_cameras(self):
        self.ui.videoCapture_comboBox.clear()
        for index in range(4):
            cap = cv2.VideoCapture(index)
            if cap is not None and cap.isOpened():
                self.ui.videoCapture_comboBox.addItem(f"Camera {index}", index)
                cap.release()
        if self.ui.videoCapture_comboBox.count() == 0:
            self.ui.videoCapture_comboBox.addItem("No Camera Found", -1)

    def populate_default_resolutions(self):
        default_resolutions = ["640x480", "800x600", "1280x720", "1920x1080"]
        self.ui.resolution_comboBox.clear()
        self.ui.resolution_comboBox.addItems(default_resolutions)

    @QtCore.pyqtSlot(dict)
    def update_drone_data(self, data):
        with QtCore.QMutexLocker(self.lock):
            for field, value in data.items():
                if field in self.field_map:
                    self.field_map[field].setPlainText(value)

                if field in self.latestData:
                    try:
                        self.latestData[field] = float(value)
                    except Exception as e:
                        logging.error(f"Error converting {field} to float: {e}")
            try:
                current_mode = str(self.droneWorker.connection.vehicle.mode) if (
                        self.droneWorker and self.droneWorker.connection.vehicle) else "N/A"
            except Exception as e:
                current_mode = ""
                logging.error(f"Mode read error: {e}")
            if "currentMode" in self.field_map:
                self.field_map["currentMode"].setPlainText(current_mode)
            if (self.latestData.get("Latitude") is not None and
                    self.latestData.get("Longitude") is not None and
                    self.latestData.get("Yaw") is not None and
                    self.mapReady):
                var_lat = self.latestData["Latitude"]
                var_lon = self.latestData["Longitude"]
                var_yaw = self.latestData["Yaw"]
                self.bridge.updateDrone.emit(var_lat, var_lon, var_yaw)
                self.routePoints.append([var_lat, var_lon])
                json_points = json.dumps(self.routePoints)
                self.bridge.updateMap.emit(json_points)

    def clear_current_state(self):
        self.ui.currentState_textEdit.clear()

    from PyQt5.QtWebEngineWidgets import QWebEngineSettings

    def init_map_view(self):
        # Eski kodu silin ve yerine bu kodu ekleyin
        self.ui.mapShown_label.setLayout(QtWidgets.QVBoxLayout())
        self.ui.mapShown_label.layout().setContentsMargins(0, 0, 0, 0)

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        map_path = os.path.join(base_dir, "app", "ui", "views", "map.html")
        url = QtCore.QUrl.fromLocalFile(map_path)
        print("Map URL:", url.toString())

        settings = self.webView.settings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        self.ui.mapShown_label.layout().addWidget(self.webView)
        self.webView.load(url)
        self.webView.show()

    @QtCore.pyqtSlot(int)
    def updateBatteryUI(self, battery_level):
        self.ui.progressBar.setValue(battery_level)
        logging.info("UI battery updated: {}%".format(battery_level))

    @QtCore.pyqtSlot(float, str)
    def updateBatteryHealth(self, health_percent, health_status):
        msg = f"Battery Health: {health_percent:.1f}% ({health_status})"
        self.ui.currentState_textEdit.append(msg)
        self.ui.currentState_textEdit.repaint()

    def closeEvent(self, event):
        if self.yolo_process and self.yolo_process.is_alive():
            self.yolo_process.terminate()
            self.yolo_process.join(timeout=1)
        if self.droneWorker is not None:
            self.droneWorker.stop()
        self.drone_controller.stopBatteryMonitoring()
        self.snap_session_folder = None
        self.snap_threadpool.waitForDone(3000)
        for handler in logging.getLogger().handlers[:]:
            logging.getLogger().removeHandler(handler)
            handler.close()
        logging.shutdown()
        super().closeEvent(event)
        event.accept()

    def exception_handler(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, RuntimeError) and "wrapped C/C++ object of type QTextEditLogger has been deleted" in str(exc_value):
            return
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
    sys.excepthook = exception_handler

    def eventFilter(self, obj, event):
        if obj == self.ui.cameraShown_label and event.type() == QtCore.QEvent.MouseButtonPress:
            self.camera_controller.process_click(event.pos())
            return True
        return super().eventFilter(obj, event)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                self.ui.snapshoot_pushButton.setEnabled(False)
                self.snap_threadpool.waitForDone(3000)
            else:
                self.ui.snapshoot_pushButton.setEnabled(True)
        super().changeEvent(event)