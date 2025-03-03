import logging
from PyQt5 import QtCore
from dronekit import connect

class DroneConnection(QtCore.QObject):
    connectionStatus = QtCore.pyqtSignal(str)
    connected = QtCore.pyqtSignal()
    connectionFailed = QtCore.pyqtSignal(str)  # Yeni sinyal

    def __init__(self, connection_str):
        super().__init__()
        self.connection_str = connection_str
        self.vehicle = None
        self.mutex = QtCore.QMutex()  # Thread-safe veri erişimi için

    def connect(self):
        # Mevcut bağlantı varsa temizle
        if self.vehicle:
            self.disconnect()

        # Async iş için worker oluştur
        worker = AsyncConnectWorker(self.connection_str)
        worker.signals.connected.connect(self._handle_connected)
        worker.signals.failed.connect(self._handle_connection_failed)
        QtCore.QThreadPool.globalInstance().start(worker)

    def _handle_connected(self, vehicle):
        with QtCore.QMutexLocker(self.mutex):
            self.vehicle = vehicle
        self.connectionStatus.emit("Connected")
        self.connected.emit()
        logging.info("Drone connection established")

    def _handle_connection_failed(self, error_msg):
        self.connectionStatus.emit("Connection Failed")
        self.connectionFailed.emit(error_msg)  # Hata detayını UI'a gönder
        logging.error(f"Connection failed: {error_msg}")

    def disconnect(self):
        try:
            if self.vehicle:
                self.vehicle.close()
                self.vehicle = None
        except Exception as e:
            logging.error(f"Disconnect error: {e}")
        finally:
            self.vehicle = None

class AsyncConnectWorker(QtCore.QRunnable):
    class Signals(QtCore.QObject):
        connected = QtCore.pyqtSignal(object)  # Vehicle objesi
        failed = QtCore.pyqtSignal(str)        # Hata mesajı

    def __init__(self, connection_str):
        super().__init__()
        self.signals = self.Signals()
        self.connection_str = connection_str

    def run(self):
        try:
            logging.info(f"Attempting async connection to {self.connection_str}")
            vehicle = connect(
                self.connection_str,
                wait_ready=True,
                timeout=100,
                baud=57600,
                heartbeat_timeout=30  # Ekstra timeout
            )
            self.signals.connected.emit(vehicle)
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            self.signals.failed.emit(error_msg)