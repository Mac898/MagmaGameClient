import sys
from Ui_main import Ui_MainWindow
import action

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class slots:
    def __init__(self, ui_main, main_logger):
        print("Loading Slots")
        self.uimain = ui_main
        self.actions = action.magmaGC_actions(self.uimain, main_logger)

        #setup slots
        self.uimain.factorioCheckBox.clicked.connect(self.actions.factorio_connect)