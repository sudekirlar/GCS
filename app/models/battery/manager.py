import logging
from PyQt5 import QtCore
from app.models.workers.battery_level import BatteryLevelWorker

class BatteryManager(QtCore.QObject):
    batteryLevelUpdated = QtCore.pyqtSignal(int)
    batteryHealthCalculated = QtCore.pyqtSignal(float, str)

    def __init__(self, vehicle=None):
        super().__init__()
        self.vehicle = vehicle
        self.battery_worker = None

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle

    def start_monitoring(self):
        if self.vehicle:
            # Güncellenmiş BatteryLevelWorker kullanılıyor.
            self.battery_worker = BatteryLevelWorker(self.vehicle)
            self.battery_worker.batteryLevelChanged.connect(self._handle_battery_level)
            self.battery_worker.batteryHealthCalculated.connect(self._handle_battery_health)
            self.battery_worker.start()

    def stop_monitoring(self):
        if self.battery_worker:
            self.battery_worker.stop()
            self.battery_worker = None

    def _handle_battery_level(self, level):
        self.batteryLevelUpdated.emit(level)
        logging.info(f"Battery Level Updated: {level}%")

    def _handle_battery_health(self, health_percent, health_status):
        self.batteryHealthCalculated.emit(health_percent, health_status)
        logging.info(f"Battery Health: {health_percent}% ({health_status})")