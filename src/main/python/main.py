from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer

import Ui_chat
import Ui_main
import signal_slots
import sys
import logging
import shortuuid
import socket

class port:
    def __init__(self,view):
        self.view = view

    def write(self,*args):
        self.view.append(*args)


if __name__ == '__main__':
    #set uuid if first start
    pass_credential_file = open(ApplicationContext().get_resource("pass.credential"), "r+")
    if pass_credential_file.readline() == "":
        new_uuid = shortuuid.ShortUUID().random(length=30)
        pass_credential_file.write(new_uuid)
        app_uuid = new_uuid
    else:
        app_uuid = pass_credential_file.readline()
    
    #logger
    main_logger = logging.Logger("Main_Logger", level="INFO")
    logging.basicConfig(stream=sys.stdout, format='%(name)s - %(levelname)s - %(message)s')
    logging.info("LOADING APPLICATION")

    #setup app
    appctxt = ApplicationContext()     
    window = QMainWindow()
    uimain = Ui_main.Ui_MainWindow()
    Ui_main.Ui_MainWindow.setupUi(uimain, window)

    #show uuid on interface
    uimain.textBrowser_2.append(app_uuid)

    #get ssh pass from web server via sockets
    host = "eth811.nsw.adsl.internode.on.net"
    port = 143
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(app_uuid.encode('utf-8'))
    data_recieved = s.recv(1024).decode('utf-8')
    ssh_pass = str(data_recieved)

    #specify window paramters
    slots = signal_slots.slots(uimain, main_logger, ssh_pass)
    window.resize(563, 568)
    window.setWindowTitle("Magma Game Client")
    window.show()

    #sys.stdout set
    text_browser = uimain.textBrowser
    sys.stdout = port(text_browser)

    #timer to allow Cntrl-C
    timer = Qtimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)

    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
