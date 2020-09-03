#sys imports
import sys
import json
import logging
import socket
import shortuuid
import time
from Crypto.Cipher import AES
#file imports
import Ui_chat
import Ui_main
import signal_slots
from PyQt5.QtWidgets import QMainWindow
#runtime imports
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.excepthook.sentry import SentryExceptionHandler
from fbs_runtime import platform
from fbs_runtime.application_context import cached_property, is_frozen

class port:
    def __init__(self,view):
        self.view = view

    def write(self,*args):
        self.view.append(*args)

class AppContext(ApplicationContext):
    @cached_property
    def exception_handlers(self):
        result = super().exception_handlers
        if is_frozen():
            result.append(self.sentry_exception_handler)
        return result
    @cached_property
    def sentry_exception_handler(self):
        return SentryExceptionHandler(
            self.build_settings['sentry_dsn'],
            self.build_settings['version'],
            self.build_settings['environment'],
            callback=self._on_sentry_init)
    def _on_sentry_init(self):
        scope = self.sentry_exception_handler.scope
        scope.set_extra('os', platform.name())    


if __name__ == '__main__':
    #set uuid if first start
    pass_credential_file = open(ApplicationContext().get_resource("pass.credential"), "r+")
    if pass_credential_file.readline() == "":
        new_uuid = shortuuid.ShortUUID().random(length=30)
        pass_credential_file.write(new_uuid)
    pass_credential_file.seek(0)
    app_uuid = pass_credential_file.readline()
    print("UUID: "+app_uuid+" FILERAW: "+pass_credential_file.readline())
    pass_credential_file.close()

    #logger
    main_logger = logging.Logger("Main_Logger", level="INFO")
    logging.basicConfig(stream=sys.stdout, format='%(name)s - %(levelname)s - %(message)s')
    print("Logger Loaded")

    #setup app
    appctxt = ApplicationContext()     
    window = QMainWindow()
    uimain = Ui_main.Ui_MainWindow()
    Ui_main.Ui_MainWindow.setupUi(uimain, window)
    print("App Started")

    #setup chat
    chat_window = Ui_chat.Ui_MainWindow()
    def enable_chat_window():
        Ui_chat.Ui_MainWindow.setupUi(chat_window, QMainWindow())
    uimain.chatButton.clicked.connect(enable_chat_window)
    print("Chat Window Prepared")
 
    #show uuid on interface
    uimain.textBrowser_2.append(app_uuid)
    print("Appended UUID to Text Browser")

    #get ssh pass from web server via sockets
    #real
    #host = "eth811.nsw.adsl.internode.on.net"
    #local test
    web_config = json.load(open(ApplicationContext().get_resource('web_config.json'),"r"))
    web_host = web_config['host']
    web_port = web_config['port']
    web_key = open(ApplicationContext().get_resource('key.key'),'rb').read().hex()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((web_host,web_port))
    aes_obj_encrypt = AES.new(web_key.encode('utf-8'), AES.MODE_CFB, web_key.encode('utf-8'))
    aes_obj_decrypt = AES.new(web_key.encode('utf-8'), AES.MODE_CFB, web_key.encode('utf-8'))
    s.sendall(app_uuid.encode('utf-8'))
    s.sendall(app_uuid.encode('utf-8'))
    print("Socket contacted")
    data_recieved = s.recv(1024)
    print("Data Recieved")
    print("DATA_REC : "+str(data_recieved))
    ssh_pass = aes_obj_decrypt.decrypt(data_recieved).decode("utf-8", errors="ignore")
    s.shutdown(socket.SHUT_WR)
    s.close()

    #specify window paramters
    slots = signal_slots.slots(uimain, main_logger, ssh_pass)
    window.resize(609, 614)
    window.setWindowTitle("Magma Game Client")
    window.show()

    #sys.stdout set
    text_browser = uimain.textBrowser
    sys.stdout = port(text_browser)

    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
