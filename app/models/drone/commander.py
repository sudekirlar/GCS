import logging
import time
from PyQt5 import QtCore
from dronekit import VehicleMode

class DroneCommander(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.vehicle = None
        self._lock = QtCore.QMutex()  # Thread-safe erişim için mutex

    @QtCore.pyqtSlot(str)
    def set_mode(self, mode_name):
        with QtCore.QMutexLocker(self._lock):
            if self.vehicle is not None:
                try:
                    new_mode = VehicleMode(mode_name)
                    self.vehicle.mode = new_mode
                    logging.info(f"Mode set to {mode_name}")
                    # Asenkron onay kontrolü başlatılıyor.
                    self._check_mode_confirmation(mode_name, start_time=time.time())
                except Exception as e:
                    logging.error(f"Error setting mode to {mode_name}: {e}")
            else:
                logging.error("Vehicle not connected, cannot set mode.")

    def _check_mode_confirmation(self, mode_name, start_time, timeout=10):
        try:
            if str(self.vehicle.mode) == mode_name:
                logging.info(f"Mode successfully changed to {mode_name}")
            elif time.time() - start_time > timeout:
                logging.error("Mode change not confirmed within timeout.")
            else:
                QtCore.QTimer.singleShot(100, lambda: self._check_mode_confirmation(mode_name, start_time, timeout))
        except Exception as e:
            logging.error(f"Error during mode confirmation check: {e}")

    @QtCore.pyqtSlot()
    def arm(self):
        with QtCore.QMutexLocker(self._lock):
            if self.vehicle is not None:
                try:
                    if not self.vehicle.is_armable:
                        logging.error("Vehicle is not armable at this time.")
                        return
                    self.vehicle.armed = True
                    logging.info("Arming command issued.")
                    self._check_arm_confirmation(start_time=time.time())
                except Exception as e:
                    logging.error(f"Error while arming: {e}")
            else:
                logging.error("Vehicle not connected, cannot arm.")

    def _check_arm_confirmation(self, start_time, timeout=10):
        try:
            if self.vehicle.armed:
                logging.info("Vehicle successfully armed.")
            elif time.time() - start_time > timeout:
                logging.error("Arming command issued, but confirmation not received within timeout.")
            else:
                QtCore.QTimer.singleShot(100, lambda: self._check_arm_confirmation(start_time, timeout))
        except Exception as e:
            logging.error(f"Error during arm confirmation check: {e}")

    @QtCore.pyqtSlot()
    def disarm(self):
        with QtCore.QMutexLocker(self._lock):
            if self.vehicle is not None:
                try:
                    self.vehicle.armed = False
                    logging.info("Disarming command issued.")
                    self._check_disarm_confirmation(start_time=time.time())
                except Exception as e:
                    logging.error(f"Error while disarming: {e}")
            else:
                logging.error("Vehicle not connected, cannot disarm.")

    def _check_disarm_confirmation(self, start_time, timeout=10):
        try:
            if not self.vehicle.armed:
                logging.info("Vehicle successfully disarmed.")
            elif time.time() - start_time > timeout:
                logging.error("Disarming command issued, but confirmation not received within timeout.")
            else:
                QtCore.QTimer.singleShot(100, lambda: self._check_disarm_confirmation(start_time, timeout))
        except Exception as e:
            logging.error(f"Error during disarm confirmation check: {e}")

    @QtCore.pyqtSlot(float)
    def takeoff(self, target_altitude):
        with QtCore.QMutexLocker(self._lock):
            if self.vehicle is not None:
                try:
                    self.vehicle.simple_takeoff(target_altitude)
                    logging.info(f"Takeoff command issued to {target_altitude} meters.")
                    self._check_takeoff_confirmation(target_altitude, start_time=time.time())
                except Exception as e:
                    logging.error(f"Error during takeoff: {e}")
            else:
                logging.error("Vehicle not connected, cannot take off.")

    def _check_takeoff_confirmation(self, target_altitude, start_time, timeout=20):
        try:
            current_alt = self.vehicle.location.global_relative_frame.alt
            logging.info(f"Current altitude: {current_alt}")
            if current_alt >= target_altitude * 0.95:
                logging.info("Target altitude reached.")
            elif time.time() - start_time > timeout:
                logging.error("Takeoff command issued, but target altitude not reached within timeout.")
            else:
                QtCore.QTimer.singleShot(500, lambda: self._check_takeoff_confirmation(target_altitude, start_time, timeout))
        except Exception as e:
            logging.error(f"Error during takeoff confirmation check: {e}")

    @QtCore.pyqtSlot()
    def land(self):
        with QtCore.QMutexLocker(self._lock):
            if self.vehicle is not None:
                try:
                    self.vehicle.mode = VehicleMode("LAND")
                    logging.info("Landing command issued.")
                    self._check_land_confirmation(start_time=time.time())
                except Exception as e:
                    logging.error(f"Error during landing: {e}")
            else:
                logging.error("Vehicle not connected, cannot land.")

    def _check_land_confirmation(self, start_time, timeout=10):
        try:
            if str(self.vehicle.mode) == "LAND":
                logging.info("Vehicle is in LAND mode.")
            elif time.time() - start_time > timeout:
                logging.error("Landing command issued, but mode not confirmed as LAND within timeout.")
            else:
                QtCore.QTimer.singleShot(100, lambda: self._check_land_confirmation(start_time, timeout))
        except Exception as e:
            logging.error(f"Error during landing confirmation check: {e}")
