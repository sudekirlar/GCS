import logging
import weakref
from PyQt5 import QtCore, Qt
from PyQt5.QtCore import QMetaObject, QRunnable

class SnapshotWorker(QRunnable):
    def __init__(self, image, file_path, parent):
        super().__init__()
        self.image = image.copy() if image is not None else None
        self.file_path = file_path
        self.parent = weakref.ref(parent)  # weak reference

    def run(self):
        try:
            if self.image is None:
                logging.error("No image provided to SnapshotWorker.")
                return
            if self.image.save(self.file_path):
                logging.info(f"Snapshot saved at {self.file_path} (worker thread)")
            else:
                logging.error(f"Failed to save snapshot image at {self.file_path}")
        except Exception as e:
            logging.exception(f"Exception in SnapshotWorker: {e}")
        finally:
            parent_obj = self.parent()
            if parent_obj is not None:
                QMetaObject.invokeMethod(parent_obj, "resetSnapInProgress", Qt.ConnectionType.QueuedConnection)
