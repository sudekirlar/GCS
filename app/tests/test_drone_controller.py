# test_drone_controller.py test için terminal kodu: python -m pytest app/tests/test_drone_controller.py -v
import os
import sys
# Proje kök dizinini (birinci_taslak_010325) Python yoluna ekle
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pytest
from unittest.mock import MagicMock, patch, call
from PyQt5 import QtCore
from app.controllers.drone_controller import DroneController

# hazırlanacak...