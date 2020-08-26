import sys
from Ui_main import Ui_MainWindow

from PyQt5.QtWidgets import *

class slots:
    def __init__(self, ui_main):
        print("Loading Slots")
        self.uimain = ui_main
        