import logging
from PyQt5 import QtCore

class DroneReader(QtCore.QObject):
    droneData = QtCore.pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.vehicle = None  # Bu, DroneConnection tarafından atanır.
        self.timer = QtCore.QTimer()

    def start_reading(self):
        self.timer.timeout.connect(self.read_drone_data)
        self.timer.start(500)

    def read_drone_data(self):
        # Öncelikle, aracın bağlı olup olmadığını kontrol ediyoruz.
        if self.vehicle is None:
            logging.warning("Vehicle is not connected. Stopping data read.")
            self.timer.stop()
            return

        try:
            data = {}
            # Attitude verisinin okunması
            try:
                attitude = self.vehicle.attitude
                data["Yaw"] = f"{attitude.yaw:.6f}" if attitude.yaw is not None else "0.000000"
                data["Roll"] = f"{attitude.roll:.6f}" if attitude.roll is not None else "0.000000"
                data["Pitch"] = f"{attitude.pitch:.6f}" if attitude.pitch is not None else "0.000000"
            except Exception as e:
                logging.error(f"Error reading attitude: {e}")
                data["Yaw"] = data["Roll"] = data["Pitch"] = "0.000000"

            # Konum verisinin okunması
            try:
                loc = self.vehicle.location.global_relative_frame
                data["Latitude"] = f"{loc.lat:.6f}" if loc.lat is not None else "0.000000"
                data["Longitude"] = f"{loc.lon:.6f}" if loc.lon is not None else "0.000000"
                data["Altitude"] = f"{loc.alt:.6f}" if loc.alt is not None else "0.000000"
            except Exception as e:
                logging.error(f"Error reading location: {e}")
                data["Latitude"] = data["Longitude"] = data["Altitude"] = "0.000000"

            # Hız bilgisinin okunması
            try:
                speed = self.vehicle.groundspeed
                data["Speed"] = f"{speed:.2f}" if speed is not None else "0.00"
            except Exception as e:
                logging.error(f"Error reading groundspeed: {e}")
                data["Speed"] = "0.00"

            # HDOP bilgisinin okunması
            try:
                hdop = self.vehicle.gps_0.eph if (hasattr(self.vehicle, "gps_0") and self.vehicle.gps_0) else None
                data["HDOP"] = f"{(hdop/100):.2f}" if hdop is not None else "0.00"
            except Exception as e:
                logging.error(f"Error reading HDOP: {e}")
                data["HDOP"] = "0.00"

            self.droneData.emit(data)
        except Exception as e:
            # Kritik bir hata meydana geldiğinde, bağlantının koptuğu varsayılır.
            logging.error(f"Critical error in reading drone data: {e}. Stopping data read.")
            self.vehicle = None
            self.timer.stop()

    def stop(self):
        self.timer.stop()