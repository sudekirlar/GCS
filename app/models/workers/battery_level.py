import logging
from PyQt5 import QtCore
from app.models.battery.calculator import BatteryHealthCalculator

class BatteryLevelWorker(QtCore.QThread):
    batteryLevelChanged = QtCore.pyqtSignal(int)
    batteryHealthCalculated = QtCore.pyqtSignal(float, str)
    finished = QtCore.pyqtSignal()

    def __init__(self, vehicle):
        super().__init__()
        self.vehicle = vehicle
        self._running = True

    def run(self):
        # Uçuş başlangıcında batarya sağlığı yalnızca bir kez kontrol ediliyor.
        try:
            battery = self.vehicle.battery
            health_percent, health_status = BatteryHealthCalculator.calculate(battery)
            self.batteryHealthCalculated.emit(health_percent, health_status)
        except Exception as e:
            logging.error(f"Battery health check error: {str(e)}")
            self.batteryHealthCalculated.emit(0.0, "Health check error")

        # Sürekli batarya seviyesi kontrolü yapılıyor.
        while self._running and self.vehicle:
            try:
                battery = self.vehicle.battery
                battery_level = battery.level
                self.batteryLevelChanged.emit(battery_level)

                # Toplam 1000ms bekleme, 100ms'lik aralıklarla kontrol
                for _ in range(10):
                    if not self._running:
                        break
                    QtCore.QThread.msleep(100)
            except Exception as e:
                logging.error(f"Battery level error: {str(e)}")
        self.cleanup()
        self.finished.emit()

    def stop(self):
        self._running = False
        if self.isRunning():
            self.quit()
            self.wait(1000)

    def cleanup(self):
        self.vehicle = None
        logging.info("BatteryLevelWorker cleanup completed.")