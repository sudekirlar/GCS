import logging
from PyQt5 import QtCore
from app.models.drone.connection import DroneConnection    # DroneConnection
from app.models.drone.reader import DroneReader            # DroneReader
from app.models.drone.commander import DroneCommander      # DroneCommander
from app.models.battery.manager import BatteryManager      # BatteryManager

class DroneDataManager(QtCore.QThread):
    droneData = QtCore.pyqtSignal(dict)
    connectionStatus = QtCore.pyqtSignal(str)
    # Eksik sinyaller eklendi ↓
    batteryLevelUpdated = QtCore.pyqtSignal(int)
    batteryHealthCalculated = QtCore.pyqtSignal(float, str)

    def __init__(self, connection_str, parent=None):
        super().__init__(parent)
        self.connection_str = connection_str
        self.connection = DroneConnection(connection_str)
        self.reader = DroneReader()
        self.commander = DroneCommander()
        self.battery_manager = BatteryManager()

        # Sinyal bağlantıları düzeltildi ↓
        self.battery_manager.batteryLevelUpdated.connect(self.batteryLevelUpdated)
        self.battery_manager.batteryHealthCalculated.connect(self.batteryHealthCalculated)
        # Sinyal bağlantıları
        self.connection.connectionStatus.connect(self.connectionStatus)
        self.connection.connected.connect(self.on_connected)
        self.reader.droneData.connect(self.droneData)

    def run(self):
        self.connection.connect()
        self.exec_()

    def on_connected(self):
        with QtCore.QMutexLocker(self.connection.mutex):  # Thread-safe erişim
            self.reader.vehicle = self.connection.vehicle
            self.commander.vehicle = self.connection.vehicle
        self.reader.start_reading()

        # Battery worker'ı başlat
        if self.connection.vehicle is not None:
            self.battery_manager.set_vehicle(self.connection.vehicle)
            self.battery_manager.start_monitoring()  # Direkt başlat

    def stop(self):
        if hasattr(self, 'battery_manager') and self.battery_manager:
            self.battery_manager.stop_monitoring()
        self.reader.stop()
        self.connection.disconnect()
        self.quit()
        self.wait(3000)  # Thread'in tamamen bitmesini bekle

    # Komut slotları
    @QtCore.pyqtSlot(str)
    def set_mode(self, mode_name):
        self.commander.set_mode(mode_name)

    @QtCore.pyqtSlot()
    def arm(self):
        self.commander.arm()

    @QtCore.pyqtSlot()
    def disarm(self):
        self.commander.disarm()

    @QtCore.pyqtSlot(float)
    def takeoff(self, target_altitude):
        self.commander.takeoff(target_altitude)

    @QtCore.pyqtSlot()
    def land(self):
        self.commander.land()