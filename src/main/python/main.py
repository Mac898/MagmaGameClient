from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import Ui_chat
import Ui_main
import signal_slots
import sys
import logging

class port:
    def __init__(self,view):
        self.view = view

    def write(self,*args):
        self.view.append(*args)


if __name__ == '__main__':
    #logger
    main_logger = logging.Logger("Main_Logger", level="INFO")
    logging.basicConfig(stream=sys.stdout, format='%(name)s - %(levelname)s - %(message)s')
    logging.info("LOADING APPLICATION")

    appctxt = ApplicationContext()     
    window = QMainWindow()
    uimain = Ui_main.Ui_MainWindow()
    Ui_main.Ui_MainWindow.setupUi(uimain, window)
    slots = signal_slots.slots(uimain, main_logger)
    window.resize(563, 568)
    window.setWindowTitle("Magma Game Client")
    window.show()

    #sys.stdout set
    text_browser = uimain.textBrowser
    sys.stdout = port(text_browser)

    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
