import logging
from PyQt5 import QtCore

class CriticalTextEditHandler(logging.Handler, QtCore.QObject):
    log_signal = QtCore.pyqtSignal(str)

    def __init__(self, text_edit):
        logging.Handler.__init__(self)
        QtCore.QObject.__init__(self)
        self.text_edit = text_edit
        self.setLevel(logging.ERROR)
        self.log_signal.connect(self.text_edit.append)

    def emit(self, record):
        try:
            msg = self.format(record)
            self.log_signal.emit(msg)
        except Exception:
            self.handleError(record)