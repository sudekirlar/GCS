import logging
from PyQt5 import QtCore, QtGui, QtWidgets
# import res
###############################################################################
# UI CLASS (Qt Designer ile gerekli güncellemeler halledildi. Tarih: 13.02.2025)
###############################################################################
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 980)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 1881, 941))
        self.widget.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #eaeaea, stop:1 #E5E4E2);;\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.openTelemetry_pushButton = QtWidgets.QPushButton(self.widget)
        self.openTelemetry_pushButton.setGeometry(QtCore.QRect(50, 210, 84, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.openTelemetry_pushButton.setFont(font)
        self.openTelemetry_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.openTelemetry_pushButton.setObjectName("openTelemetry_pushButton")
        self.closeTelemetry_pushButton = QtWidgets.QPushButton(self.widget)
        self.closeTelemetry_pushButton.setGeometry(QtCore.QRect(160, 210, 84, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.closeTelemetry_pushButton.setFont(font)
        self.closeTelemetry_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.closeTelemetry_pushButton.setObjectName("closeTelemetry_pushButton")
        self.map_label = QtWidgets.QLabel(self.widget)
        self.map_label.setGeometry(QtCore.QRect(280, 350, 165, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.map_label.setFont(font)
        self.map_label.setObjectName("map_label")
        self.mapShown_label = QtWidgets.QLabel(self.widget)
        self.mapShown_label.setGeometry(QtCore.QRect(280, 380, 661, 351))
        self.mapShown_label.setStyleSheet("border: 1px solid;\n"
"border-color: black;")
        self.mapShown_label.setText("")
        self.mapShown_label.setObjectName("mapShown_label")
        self.addMarker_pushButton = QtWidgets.QPushButton(self.widget)
        self.addMarker_pushButton.setGeometry(QtCore.QRect(770, 350, 84, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(7)
        self.addMarker_pushButton.setFont(font)
        self.addMarker_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.addMarker_pushButton.setObjectName("addMarker_pushButton")
        self.clearMarker_pushButton = QtWidgets.QPushButton(self.widget)
        self.clearMarker_pushButton.setGeometry(QtCore.QRect(860, 350, 84, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(7)
        self.clearMarker_pushButton.setFont(font)
        self.clearMarker_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.clearMarker_pushButton.setObjectName("clearMarker_pushButton")
        self.videoCapture_label = QtWidgets.QLabel(self.widget)
        self.videoCapture_label.setGeometry(QtCore.QRect(51, 311, 191, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.videoCapture_label.setFont(font)
        self.videoCapture_label.setObjectName("videoCapture_label")
        self.videoCapture_comboBox = QtWidgets.QComboBox(self.widget)
        self.videoCapture_comboBox.setGeometry(QtCore.QRect(50, 350, 191, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.videoCapture_comboBox.setFont(font)
        self.videoCapture_comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #797979, stop:0.48 #696969, stop:0.52 #5e5e5e, stop:1 #4f4f4f);\n"
"    padding: 1px 23px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı fontu ayarlandı */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    color: white;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5e5e5e, stop:1 #4f4f4f); /* Düşme menüsü için gradient */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/images/Adsız tasarım (54).png); /* Ok simgesi yolu */\n"
"    width: 12px; /* Ok simgesinin boyutu */\n"
"    height: 12px;\n"
"    margin: 5px; /* Simgenin etrafındaki boşluk */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #4f4f4f;\n"
"    color: #ffffff; /* Seçeneklerin rengi beyaza ayarlandı */\n"
"    font-family: \"Segoe UI Semibold\"; /* Seçenek yazı fontu ayarlandı */\n"
"\n"
"    selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"}\n"
"")
        self.videoCapture_comboBox.setObjectName("videoCapture_comboBox")
        self.resolution_label = QtWidgets.QLabel(self.widget)
        self.resolution_label.setGeometry(QtCore.QRect(51, 391, 191, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.resolution_label.setFont(font)
        self.resolution_label.setObjectName("resolution_label")
        self.resolution_comboBox = QtWidgets.QComboBox(self.widget)
        self.resolution_comboBox.setGeometry(QtCore.QRect(50, 430, 191, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.resolution_comboBox.setFont(font)
        self.resolution_comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #797979, stop:0.48 #696969, stop:0.52 #5e5e5e, stop:1 #4f4f4f);\n"
"    padding: 1px 23px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı fontu ayarlandı */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    color: white;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5e5e5e, stop:1 #4f4f4f); /* Düşme menüsü için gradient */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/images/Adsız tasarım (54).png); /* Ok simgesi yolu */\n"
"    width: 12px; /* Ok simgesinin boyutu */\n"
"    height: 12px;\n"
"    margin: 5px; /* Simgenin etrafındaki boşluk */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #4f4f4f;\n"
"    color: #ffffff; /* Seçeneklerin rengi beyaza ayarlandı */\n"
"    font-family: \"Segoe UI Semibold\"; /* Seçenek yazı fontu ayarlandı */\n"
"\n"
"    selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"}\n"
"")
        self.resolution_comboBox.setObjectName("resolution_comboBox")
        self.openCamera_pushButton = QtWidgets.QPushButton(self.widget)
        self.openCamera_pushButton.setGeometry(QtCore.QRect(50, 480, 84, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.openCamera_pushButton.setFont(font)
        self.openCamera_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.openCamera_pushButton.setObjectName("openCamera_pushButton")
        self.closeCamera_pushButton = QtWidgets.QPushButton(self.widget)
        self.closeCamera_pushButton.setGeometry(QtCore.QRect(160, 480, 84, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.closeCamera_pushButton.setFont(font)
        self.closeCamera_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.closeCamera_pushButton.setObjectName("closeCamera_pushButton")
        self.cameraShown_label = QtWidgets.QLabel(self.widget)
        self.cameraShown_label.setGeometry(QtCore.QRect(970, 50, 891, 521))
        self.cameraShown_label.setStyleSheet("border: 1px solid;\n"
"border-color: black;")
        self.cameraShown_label.setText("")
        self.cameraShown_label.setObjectName("cameraShown_label")
        self.camera_label = QtWidgets.QLabel(self.widget)
        self.camera_label.setGeometry(QtCore.QRect(970, 20, 165, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.camera_label.setFont(font)
        self.camera_label.setObjectName("camera_label")
        self.bodyDetectedShown_label = QtWidgets.QLabel(self.widget)
        self.bodyDetectedShown_label.setGeometry(QtCore.QRect(950, 620, 300, 300))
        self.bodyDetectedShown_label.setStyleSheet("border: 1px solid;\n"
"border-color: black;")
        self.bodyDetectedShown_label.setText("")
        self.bodyDetectedShown_label.setObjectName("bodyDetectedShown_label")
        self.woundDetectedShown_label = QtWidgets.QLabel(self.widget)
        self.woundDetectedShown_label.setGeometry(QtCore.QRect(1260, 620, 300, 300))
        self.woundDetectedShown_label.setStyleSheet("border: 1px solid;\n"
"border-color: black;")
        self.woundDetectedShown_label.setText("")
        self.woundDetectedShown_label.setObjectName("woundDetectedShown_label")
        self.snapshoot_pushButton = QtWidgets.QPushButton(self.widget)
        self.snapshoot_pushButton.setGeometry(QtCore.QRect(1713, 20, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(7)
        self.snapshoot_pushButton.setFont(font)
        self.snapshoot_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.snapshoot_pushButton.setObjectName("snapshoot_pushButton")
        self.bodyDetected_label = QtWidgets.QLabel(self.widget)
        self.bodyDetected_label.setGeometry(QtCore.QRect(950, 590, 165, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bodyDetected_label.setFont(font)
        self.bodyDetected_label.setObjectName("bodyDetected_label")
        self.woundDetected_label = QtWidgets.QLabel(self.widget)
        self.woundDetected_label.setGeometry(QtCore.QRect(1260, 590, 165, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.woundDetected_label.setFont(font)
        self.woundDetected_label.setObjectName("woundDetected_label")
        self.fireDetectedShown_label = QtWidgets.QLabel(self.widget)
        self.fireDetectedShown_label.setGeometry(QtCore.QRect(1570, 620, 300, 300))
        self.fireDetectedShown_label.setStyleSheet("border: 1px solid;\n"
"border-color: black;")
        self.fireDetectedShown_label.setText("")
        self.fireDetectedShown_label.setObjectName("fireDetectedShown_label")
        self.fireDetected_label = QtWidgets.QLabel(self.widget)
        self.fireDetected_label.setGeometry(QtCore.QRect(1570, 590, 165, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fireDetected_label.setFont(font)
        self.fireDetected_label.setObjectName("fireDetected_label")
        self.clearPath_pushButton = QtWidgets.QPushButton(self.widget)
        self.clearPath_pushButton.setGeometry(QtCore.QRect(680, 350, 84, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(7)
        self.clearPath_pushButton.setFont(font)
        self.clearPath_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.clearPath_pushButton.setObjectName("clearPath_pushButton")
        self.goToFocus_pushButton = QtWidgets.QPushButton(self.widget)
        self.goToFocus_pushButton.setGeometry(QtCore.QRect(590, 350, 84, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(7)
        self.goToFocus_pushButton.setFont(font)
        self.goToFocus_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.goToFocus_pushButton.setObjectName("goToFocus_pushButton")
        self.mode_label = QtWidgets.QLabel(self.widget)
        self.mode_label.setGeometry(QtCore.QRect(51, 590, 165, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mode_label.setFont(font)
        self.mode_label.setObjectName("mode_label")
        self.mode_comboBox = QtWidgets.QComboBox(self.widget)
        self.mode_comboBox.setGeometry(QtCore.QRect(50, 630, 191, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.mode_comboBox.setFont(font)
        self.mode_comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #797979, stop:0.48 #696969, stop:0.52 #5e5e5e, stop:1 #4f4f4f);\n"
"    padding: 1px 23px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı fontu ayarlandı */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    color: white;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5e5e5e, stop:1 #4f4f4f); /* Düşme menüsü için gradient */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/images/Adsız tasarım (54).png); /* Ok simgesi yolu */\n"
"    width: 12px; /* Ok simgesinin boyutu */\n"
"    height: 12px;\n"
"    margin: 5px; /* Simgenin etrafındaki boşluk */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #4f4f4f;\n"
"    color: #ffffff; /* Seçeneklerin rengi beyaza ayarlandı */\n"
"    font-family: \"Segoe UI Semibold\"; /* Seçenek yazı fontu ayarlandı */\n"
"\n"
"    selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"}\n"
"")
        self.mode_comboBox.setObjectName("mode_comboBox")
        self.mode_comboBox.addItem("GUIDED")
        self.mode_comboBox.addItem("STABILIZE")
        self.mode_comboBox.addItem("AUTO")
        self.mode_comboBox.addItem("LOITER")
        self.changeMode_pushButton = QtWidgets.QPushButton(self.widget)
        self.changeMode_pushButton.setGeometry(QtCore.QRect(50, 670, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.changeMode_pushButton.setFont(font)
        self.changeMode_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.changeMode_pushButton.setObjectName("changeMode_pushButton")
        self.mode_label_2 = QtWidgets.QLabel(self.widget)
        self.mode_label_2.setGeometry(QtCore.QRect(280, 750, 165, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mode_label_2.setFont(font)
        self.mode_label_2.setObjectName("mode_label_2")
        self.arm_pushButton = QtWidgets.QPushButton(self.widget)
        self.arm_pushButton.setGeometry(QtCore.QRect(280, 780, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.arm_pushButton.setFont(font)
        self.arm_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.arm_pushButton.setObjectName("arm_pushButton")
        self.disarm_pushButton = QtWidgets.QPushButton(self.widget)
        self.disarm_pushButton.setGeometry(QtCore.QRect(410, 780, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.disarm_pushButton.setFont(font)
        self.disarm_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.disarm_pushButton.setObjectName("disarm_pushButton")
        self.takeOff_pushButton = QtWidgets.QPushButton(self.widget)
        self.takeOff_pushButton.setGeometry(QtCore.QRect(280, 820, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.takeOff_pushButton.setFont(font)
        self.takeOff_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.takeOff_pushButton.setObjectName("takeOff_pushButton")
        self.land_pushButton = QtWidgets.QPushButton(self.widget)
        self.land_pushButton.setGeometry(QtCore.QRect(410, 820, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.land_pushButton.setFont(font)
        self.land_pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #333333; /* Combobox ile uyumlu renk */\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:0.48 #696969, \n"
"                                stop:0.52 #5e5e5e, stop:1 #4f4f4f); /* Combobox gradyanı */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı tipi */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #5e5e5e, stop:1 #797979); /* Hafif ters gradyan efekti */\n"
"    border: 2px solid #555555; /* Basıldığında daha koyu kenar */\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* Flat düğme için kenar kaldırıldı */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #797979, stop:1 #4f4f4f); /* Flat durumda da gradyan */\n"
"    color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #898989, stop:1 #5e5e5e); /* Daha açık gradyan efekti */\n"
"    font-weight: bold; /* Varsayılan düğme yazısını vurgulama */\n"
"}\n"
"")
        self.land_pushButton.setObjectName("land_pushButton")
        self.criticalShown_textEdit = QtWidgets.QTextEdit(self.widget)
        self.criticalShown_textEdit.setGeometry(QtCore.QRect(580, 780, 331, 141))
        self.criticalShown_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.criticalShown_textEdit.setObjectName("criticalShown_textEdit")
        self.criticalLogs_label = QtWidgets.QLabel(self.widget)
        self.criticalLogs_label.setGeometry(QtCore.QRect(580, 750, 165, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.criticalLogs_label.setFont(font)
        self.criticalLogs_label.setObjectName("criticalLogs_label")
        self.altitudeLineEdit = QtWidgets.QLineEdit(self.widget)
        self.altitudeLineEdit.setGeometry(QtCore.QRect(40, 720, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.altitudeLineEdit.setFont(font)
        self.altitudeLineEdit.setObjectName("altitudeLineEdit")
        self.comPortTelemetry_label = QtWidgets.QLabel(self.widget)
        self.comPortTelemetry_label.setGeometry(QtCore.QRect(51, 111, 191, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comPortTelemetry_label.setFont(font)
        self.comPortTelemetry_label.setObjectName("comPortTelemetry_label")
        self.comPortTelemetry_comboBox = QtWidgets.QComboBox(self.widget)
        self.comPortTelemetry_comboBox.setGeometry(QtCore.QRect(50, 150, 191, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.comPortTelemetry_comboBox.setFont(font)
        self.comPortTelemetry_comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #797979, stop:0.48 #696969, stop:0.52 #5e5e5e, stop:1 #4f4f4f);\n"
"    padding: 1px 23px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI Semibold\"; /* Yazı fontu ayarlandı */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    color: white;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5e5e5e, stop:1 #4f4f4f); /* Düşme menüsü için gradient */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/images/Adsız tasarım (54).png); /* Ok simgesi yolu */\n"
"    width: 12px; /* Ok simgesinin boyutu */\n"
"    height: 12px;\n"
"    margin: 5px; /* Simgenin etrafındaki boşluk */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #4f4f4f;\n"
"    color: #ffffff; /* Seçeneklerin rengi beyaza ayarlandı */\n"
"    font-family: \"Segoe UI Semibold\"; /* Seçenek yazı fontu ayarlandı */\n"
"\n"
"    selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"}\n"
"")
        self.comPortTelemetry_comboBox.setObjectName("comPortTelemetry_comboBox")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(50, 70, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.batteryLevel_label = QtWidgets.QLabel(self.widget)
        self.batteryLevel_label.setGeometry(QtCore.QRect(50, 30, 191, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batteryLevel_label.setFont(font)
        self.batteryLevel_label.setObjectName("batteryLevel_label")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(20, 280, 241, 2))
        self.line.setStyleSheet("background-color: #000000;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(20, 560, 241, 2))
        self.line_2.setStyleSheet("background-color: #000000;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, -10, 471, 89))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yaw_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yaw_label.setFont(font)
        self.yaw_label.setObjectName("yaw_label")
        self.horizontalLayout.addWidget(self.yaw_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pitch_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pitch_label.setFont(font)
        self.pitch_label.setObjectName("pitch_label")
        self.horizontalLayout.addWidget(self.pitch_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.roll_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.roll_label.setFont(font)
        self.roll_label.setObjectName("roll_label")
        self.horizontalLayout.addWidget(self.roll_label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(280, 48, 641, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.yaw_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.yaw_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.yaw_textEdit.setObjectName("yaw_textEdit")
        self.horizontalLayout_2.addWidget(self.yaw_textEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pitch_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.pitch_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.pitch_textEdit.setObjectName("pitch_textEdit")
        self.horizontalLayout_2.addWidget(self.pitch_textEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.roll_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.roll_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.roll_textEdit.setObjectName("roll_textEdit")
        self.horizontalLayout_2.addWidget(self.roll_textEdit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(280, 90, 511, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.latitude_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.latitude_label.setFont(font)
        self.latitude_label.setObjectName("latitude_label")
        self.horizontalLayout_3.addWidget(self.latitude_label)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.logitude_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logitude_label.setFont(font)
        self.logitude_label.setObjectName("logitude_label")
        self.horizontalLayout_3.addWidget(self.logitude_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.altitude_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.altitude_label.setFont(font)
        self.altitude_label.setObjectName("altitude_label")
        self.horizontalLayout_3.addWidget(self.altitude_label)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(280, 130, 641, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.latitude_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_4)
        self.latitude_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.latitude_textEdit.setObjectName("latitude_textEdit")
        self.horizontalLayout_4.addWidget(self.latitude_textEdit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.longitude_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_4)
        self.longitude_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.longitude_textEdit.setObjectName("longitude_textEdit")
        self.horizontalLayout_4.addWidget(self.longitude_textEdit)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.altitude_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_4)
        self.altitude_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.altitude_textEdit.setObjectName("altitude_textEdit")
        self.horizontalLayout_4.addWidget(self.altitude_textEdit)
        self.currentState_label = QtWidgets.QLabel(self.widget)
        self.currentState_label.setGeometry(QtCore.QRect(280, 270, 316, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.currentState_label.setFont(font)
        self.currentState_label.setObjectName("currentState_label")
        self.currentState_textEdit = QtWidgets.QTextEdit(self.widget)
        self.currentState_textEdit.setGeometry(QtCore.QRect(280, 300, 641, 31))
        self.currentState_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.currentState_textEdit.setObjectName("currentState_textEdit")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(280, 180, 511, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.speed_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.speed_label.setFont(font)
        self.speed_label.setObjectName("speed_label")
        self.horizontalLayout_5.addWidget(self.speed_label)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.hdop_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hdop_label.setFont(font)
        self.hdop_label.setObjectName("hdop_label")
        self.horizontalLayout_5.addWidget(self.hdop_label)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.currentMode_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.currentMode_label.setFont(font)
        self.currentMode_label.setObjectName("currentMode_label")
        self.horizontalLayout_5.addWidget(self.currentMode_label)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(280, 220, 641, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.speed_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_6)
        self.speed_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.speed_textEdit.setObjectName("speed_textEdit")
        self.horizontalLayout_6.addWidget(self.speed_textEdit)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.hdop_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_6)
        self.hdop_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.hdop_textEdit.setObjectName("hdop_textEdit")
        self.horizontalLayout_6.addWidget(self.hdop_textEdit)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.currentMode_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_6)
        self.currentMode_textEdit.setStyleSheet("background-color: #D3D3D3;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"color: #1B1212;")
        self.currentMode_textEdit.setObjectName("currentMode_textEdit")
        self.horizontalLayout_6.addWidget(self.currentMode_textEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.openTelemetry_pushButton.setText(_translate("Form", "Open"))
        self.closeTelemetry_pushButton.setText(_translate("Form", "Close"))
        self.map_label.setText(_translate("Form", "Map"))
        self.addMarker_pushButton.setText(_translate("Form", "Add Marker"))
        self.clearMarker_pushButton.setText(_translate("Form", "Clear Marker"))
        self.videoCapture_label.setText(_translate("Form", "Video Capture"))
        self.resolution_label.setText(_translate("Form", "Resolution"))
        self.openCamera_pushButton.setText(_translate("Form", "Open"))
        self.closeCamera_pushButton.setText(_translate("Form", "Close"))
        self.camera_label.setText(_translate("Form", "Camera"))
        self.snapshoot_pushButton.setText(_translate("Form", "Snapshoot!"))
        self.bodyDetected_label.setText(_translate("Form", "Body Detected:"))
        self.woundDetected_label.setText(_translate("Form", "Wound Detected:"))
        self.fireDetected_label.setText(_translate("Form", "Fire Detected:"))
        self.clearPath_pushButton.setText(_translate("Form", "Clear Path"))
        self.goToFocus_pushButton.setText(_translate("Form", "Go to Focus"))
        self.mode_label.setText(_translate("Form", "Change Mode"))
        self.changeMode_pushButton.setText(_translate("Form", "Apply Mode"))
        self.mode_label_2.setText(_translate("Form", "Commands:"))
        self.arm_pushButton.setText(_translate("Form", "Arm"))
        self.disarm_pushButton.setText(_translate("Form", "Disarm"))
        self.takeOff_pushButton.setText(_translate("Form", "Takeoff"))
        self.land_pushButton.setText(_translate("Form", "Land"))
        self.criticalShown_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.criticalLogs_label.setText(_translate("Form", "Critical Logs:"))
        self.altitudeLineEdit.setText(_translate("Form", "3 meters for takeoff"))
        self.comPortTelemetry_label.setText(_translate("Form", "COM Ports"))
        self.batteryLevel_label.setText(_translate("Form", "Battery Level"))
        self.yaw_label.setText(_translate("Form", "Yaw"))
        self.pitch_label.setText(_translate("Form", "Pitch"))
        self.roll_label.setText(_translate("Form", "Roll"))
        self.yaw_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pitch_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.roll_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.latitude_label.setText(_translate("Form", "Latitude"))
        self.logitude_label.setText(_translate("Form", "Longitude"))
        self.altitude_label.setText(_translate("Form", "Altitude"))
        self.latitude_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.longitude_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.altitude_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.currentState_label.setText(_translate("Form", "Current State"))
        self.currentState_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.speed_label.setText(_translate("Form", "Speed"))
        self.hdop_label.setText(_translate("Form", "HDOP"))
        self.currentMode_label.setText(_translate("Form", "Mode"))
        self.speed_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.hdop_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.currentMode_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))