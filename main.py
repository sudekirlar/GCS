import sys
import multiprocessing as mp
from PyQt5 import QtWidgets
from app.ui.main_window import SerialMonitor

if __name__ == '__main__':
    import multiprocessing as mp
    mp.set_start_method('spawn')
    app = QtWidgets.QApplication(sys.argv)
    window = SerialMonitor()
    window.show()
    sys.exit(app.exec_())