from PyQt5 import QtCore

class Bridge(QtCore.QObject):
    updateDrone = QtCore.pyqtSignal(float, float, float)  # latitude, longitude, yaw
    addMarker = QtCore.pyqtSignal(float, float)  # latitude, longitude
    clearMarkers = QtCore.pyqtSignal()
    updateMap = QtCore.pyqtSignal(str)  # JSON string şeklinde routePoints
    goToFocus = QtCore.pyqtSignal()  # Go To Focus butonu sinyali
    clearPath = QtCore.pyqtSignal()  # Clear Path butonu sinyali