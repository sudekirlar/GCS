import os
import logging
from datetime import datetime
from PyQt5 import QtCore
from app.models.workers.snapshot import SnapshotWorker  # SnapshotWorker importu

class SnapshotController:
    def __init__(self, parent):
        self.parent = parent

    def snapshoot(self):
        if self.parent.video_worker is None:
            logging.error("Camera is closed. Cannot snapshoot.")
            return
        self.parent.frame_lock.lock()
        frame = self.parent.current_frame.copy() if self.parent.current_frame is not None else None
        self.parent.frame_lock.unlock()
        if frame is None:
            logging.error("No frame available to snapshoot.")
            return
        if self.parent.snap_in_progress:
            logging.warning("Snapshoot already in progress. Skipping new snapshoot.")
            return
        self.parent.snap_in_progress = True
        self.parent.ui.snapshoot_pushButton.setEnabled(False)
        self.parent.ui.snapshoot_pushButton.setStyleSheet("background-color: #F44336; color: white;")
        if self.parent.snap_session_folder is None:
            timestamp = datetime.now().strftime("%d.%m.%Y %H-%M")
            self.parent.snap_session_folder = os.path.join(self.parent.snap_base_dir, timestamp)
            try:
                os.makedirs(self.parent.snap_session_folder, exist_ok=False)
            except Exception as e:
                logging.error(f"Error creating snapshoot session folder {self.parent.snap_session_folder}: {e}")
                self.parent.snap_in_progress = False
                self.parent.ui.snapshoot_pushButton.setEnabled(True)
                self.parent.ui.snapshoot_pushButton.setStyleSheet("")
                return
        photo_timestamp = datetime.now().strftime("%H-%M-%S")
        file_name = f"photo {photo_timestamp}.png"
        file_path = os.path.join(self.parent.snap_session_folder, file_name)
        snap_worker = SnapshotWorker(frame, file_path, self.parent)
        self.parent.snap_threadpool.start(snap_worker)

    def resetSnapInProgress(self):
        QtCore.QTimer.singleShot(2000, self._resetSnapInProgress)

    def _resetSnapInProgress(self):
        self.parent.snap_in_progress = False
        self.parent.ui.snapshoot_pushButton.setEnabled(True)
        self.parent.ui.snapshoot_pushButton.setStyleSheet("")