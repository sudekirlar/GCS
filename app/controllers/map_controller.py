import os
import logging
from PyQt5 import QtCore, QtWebEngineWidgets, QtWebChannel
from app.services.bridge import Bridge  # Bridge sınıfı importu

class MapController:
    def __init__(self, parent):
        self.parent = parent

    def init_map_view(self):
        # QWebEngineView widget'ını ana widget içinde oluşturuyoruz
        self.parent.webView = QtWebEngineWidgets.QWebEngineView(self.parent.ui.widget)
        self.parent.webView.setGeometry(QtCore.QRect(280, 380, 661, 351))
        self.parent.webView.show()

        # __file__'a göre map.html dosyasının bulunduğu klasörü belirleyelim
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ui", "views"))
        map_path = os.path.join(base_dir, "map.html")
        logging.info("Loading map from: %s", map_path)
        self.parent.webView.load(QtCore.QUrl.fromLocalFile(map_path))
        self.parent.webView.loadFinished.connect(self.on_map_load_finished)

        # QWebChannel kurulumunu yapıyoruz
        self.parent.bridge = Bridge()
        self.parent.channel = QtWebChannel.QWebChannel()
        self.parent.channel.registerObject('bridge', self.parent.bridge)
        self.parent.webView.page().setWebChannel(self.parent.channel)

    def on_map_load_finished(self, ok):
        if ok:
            logging.info("Map finished loading.")
            self.parent.mapReady = True
        else:
            logging.error("Map failed to load.")

    def add_marker(self):
        lat = self.parent.latestData.get("Latitude")
        lon = self.parent.latestData.get("Longitude")
        if lat is not None and lon is not None:
            self.parent.bridge.addMarker.emit(lat, lon)
            logging.info(f"Add Marker emitted for ({lat}, {lon})")

    def clear_markers(self):
        self.parent.bridge.clearMarkers.emit()
        logging.info("Clear Markers emitted")

    def go_to_focus(self):
        self.parent.bridge.goToFocus.emit()
        logging.info("GoToFocus emitted.")

    def clear_path(self):
        self.parent.routePoints = []
        self.parent.bridge.clearPath.emit()
        logging.info("ClearPath emitted and routePoints cleared.")
