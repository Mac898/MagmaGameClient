import sys
from Ui_main import Ui_MainWindow
import action

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class slots:
    def __init__(self, ui_main, main_logger, ssh_pass):
        print("Loading Slots")
        self.uimain = ui_main
        self.actions = action.magmaGC_actions(self.uimain, main_logger, ssh_pass)

        #define list of custom checkboxes
        custom_checkbox_list = [self.uimain.checkBox, self.uimain.checkBox_2, self.uimain.checkBox_3, self.uimain.checkBox_4, self.uimain.checkBox_5]

        #setup slots
        self.uimain.factorioCheckBox.clicked.connect(self.actions.factorio_connect)
        self.uimain.minecraftCheckBox.clicked.connect(self.actions.minecraft_connect)

        #custom forwarding slots
        self.uimain.checkBox.clicked.connect(lambda: self.actions.custom_connect(1, self.uimain.lineEdit.text(), custom_checkbox_list))
        self.uimain.checkBox_2.clicked.connect(lambda: self.actions.custom_connect(2, self.uimain.lineEdit_2.text(), custom_checkbox_list))
        self.uimain.checkBox_3.clicked.connect(lambda: self.actions.custom_connect(3, self.uimain.lineEdit_3.text(), custom_checkbox_list))
        self.uimain.checkBox_4.clicked.connect(lambda: self.actions.custom_connect(4, self.uimain.lineEdit_4.text(), custom_checkbox_list))
        self.uimain.checkBox_5.clicked.connect(lambda: self.actions.custom_connect(5, self.uimain.lineEdit_5.text(), custom_checkbox_list))
