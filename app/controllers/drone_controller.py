import logging
from PyQt5 import QtCore
from app.services.drone_data import DroneDataManager  # DroneDataManager importu
from app.models.battery.manager import BatteryManager  # BatteryManager importu (eğer kullanılıyorsa)

class DroneController:
    def __init__(self, parent):
        self.parent = parent  # parent, SerialMonitor örneği
    def open_port(self):
        selected_port = self.parent.ui.comPortTelemetry_comboBox.currentText()
        # TCP/COM ayrımı yap
        if selected_port.startswith("TCP:"):
            connection_str = selected_port.lower().replace("tcp:", "tcp:")
        else:
            connection_str = selected_port
        try:
            self.parent.droneWorker = DroneDataManager(connection_str)
            self.parent.droneWorker.connectionStatus.connect(
                lambda status: self.parent.ui.currentState_textEdit.append(f"Drone status: {status}")
            )
            self.parent.droneWorker.droneData.connect(self.parent.update_drone_data)
            self.parent.droneWorker.start()
            self.parent.ui.currentState_textEdit.append(f"Attempting connection to {connection_str}...")
            logging.info(f"Attempting connection to {connection_str}")
            # UI güncellemeleri
            self.parent.ui.openTelemetry_pushButton.setEnabled(False)
            self.parent.ui.closeTelemetry_pushButton.setEnabled(True)
            self.parent.ui.openTelemetry_pushButton.setStyleSheet("background-color: #4CAF50; color: white;")
            self.parent.ui.closeTelemetry_pushButton.setStyleSheet("")
            self.startBatteryMonitoring()
        except Exception as e:
            error_msg = f"Connection failed: {str(e)}"
            self.parent.ui.currentState_textEdit.append(error_msg)
            logging.error(error_msg)
            self.parent.ui.openTelemetry_pushButton.setEnabled(True)

    def close_port(self):
        if self.parent.droneWorker is not None:
            self.parent.droneWorker.stop()
            self.parent.droneWorker = None
            self.parent.ui.currentState_textEdit.append("Drone connection closed.")
            logging.info("Drone connection closed.")
            self.parent.ui.openTelemetry_pushButton.setEnabled(True)
            self.parent.ui.closeTelemetry_pushButton.setEnabled(False)
            self.parent.ui.closeTelemetry_pushButton.setStyleSheet("background-color: #F44336; color: white;")
            self.parent.ui.openTelemetry_pushButton.setStyleSheet("")
            self.stopBatteryMonitoring()

    def on_change_mode_clicked(self):
        if self.parent.droneWorker:
            mode = self.parent.ui.mode_comboBox.currentText()
            QtCore.QMetaObject.invokeMethod(
                self.parent.droneWorker, "set_mode", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, mode)
            )
            self.parent.ui.currentState_textEdit.append(f"Mode changed to {mode}.")
            logging.info(f"Mode changed to {mode}.")

    def on_arm_clicked(self):
        if self.parent.droneWorker:
            QtCore.QMetaObject.invokeMethod(
                self.parent.droneWorker, "arm", QtCore.Qt.QueuedConnection
            )
            self.parent.ui.currentState_textEdit.append("Vehicle armed.")
            logging.info("Vehicle armed.")

    def on_disarm_clicked(self):
        if self.parent.droneWorker:
            QtCore.QMetaObject.invokeMethod(
                self.parent.droneWorker, "disarm", QtCore.Qt.QueuedConnection
            )
            self.parent.ui.currentState_textEdit.append("Vehicle disarmed.")
            logging.info("Vehicle disarmed.")

    def on_takeoff_clicked(self):
        if self.parent.droneWorker:
            try:
                alt = float(self.parent.ui.altitudeLineEdit.text())
            except ValueError:
                alt = 3.0
            QtCore.QMetaObject.invokeMethod(
                self.parent.droneWorker, "takeoff", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(float, alt)
            )
            self.parent.ui.currentState_textEdit.append(f"Taking off to {alt} meters.")
            logging.info(f"Taking off to {alt} meters.")

    def on_land_clicked(self):
        if self.parent.droneWorker:
            QtCore.QMetaObject.invokeMethod(
                self.parent.droneWorker, "land", QtCore.Qt.QueuedConnection
            )
            self.parent.ui.currentState_textEdit.append("Vehicle landing.")
            logging.info("Vehicle landing command issued.")

    def update_current_mode(self):
        if self.parent.droneWorker and self.parent.droneWorker.connection.vehicle:
            try:
                current_mode = str(self.parent.droneWorker.connection.vehicle.mode)
            except Exception as e:
                current_mode = "N/A"
                logging.error(f"Error reading current mode: {e}")
        else:
            current_mode = "N/A"
        if "currentMode" in self.parent.field_map:
            self.parent.field_map["currentMode"].setPlainText(current_mode)
            logging.info(f"Current mode updated (via timer): {current_mode}")

    def startBatteryMonitoring(self):
        if self.parent.droneWorker:
            self.parent.droneWorker.batteryLevelUpdated.connect(self.parent.updateBatteryUI)
            self.parent.droneWorker.batteryHealthCalculated.connect(self.parent.updateBatteryHealth)

    def stopBatteryMonitoring(self):
        if self.parent.droneWorker:
            try:
                self.parent.droneWorker.batteryLevelUpdated.disconnect()
                self.parent.droneWorker.batteryHealthCalculated.disconnect()
            except Exception:
                pass