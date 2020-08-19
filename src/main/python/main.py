from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import Ui_chat
import Ui_main
import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = QMainWindow()
    uimain = Ui_main.Ui_MainWindow()
    Ui_main.Ui_MainWindow.setupUi(uimain, window)
    window.resize(563, 568)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)