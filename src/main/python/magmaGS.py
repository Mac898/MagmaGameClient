from sshtunnel import SSHTunnelForwarder, create_logger as SSHTF_create_logger
import json
import main
from fbs_runtime.application_context.PyQt5 import ApplicationContext

class magmaGS:
    def __init__(self, main_logger, ssh_pass):
        self.main_logger = main_logger
        #define settings from config
        self.remote_list = [("127.0.0.1",6969)]
        self.local_list = [("127.0.0.1",6969)]
        self.creds_pass = ssh_pass
        self.ssh_config_file = open(ApplicationContext().get_resource("ssh_config.json"))
        self.ssh_config = json.load(self.ssh_config_file)
        self.ssh_hostname = self.ssh_config['hostname']
        self.ssh_port = self.ssh_config['port']
        self.ssh_user = self.ssh_config['username']
        print(self.ssh_config)

        #create loggger
        SSHTF_create_logger(loglevel="DEBUG", logger=main_logger)


        #establish sshtunnel server
        self.server = SSHTunnelForwarder(
            self.ssh_hostname,
            ssh_port=self.ssh_port,
            ssh_username=self.ssh_user,
            ssh_password=self.creds_pass,
            remote_bind_addresses=self.remote_list,
            local_bind_addresses=self.local_list
        )

    #add remote bind
    def add_remote_bind(self, local_bind, remote_bind, ip="127.0.0.1"):
        to_add = (ip, int(remote_bind))
        to_add_local = (ip, int(local_bind))
        self.remote_list.append(to_add)
        self.local_list.append(to_add_local)
        print("Adding remote bind: "+str(to_add))
        
    #remove remote bind
    def remove_remote_bind(self, local_bind, remote_bind, ip="127.0.0.1"):
        to_remove = (ip, int(remote_bind))
        to_remove_local = (ip, int(local_bind))
        print("Removing remote bind: "+str(to_remove))
        try:
            self.remote_list.remove(to_remove)
            self.remote_list.remove(to_remove_local)
        except ValueError:
            print("Tried to remove bind from list before addition")

    #control tunnel
    def start(self):
        self.server.start()
        print("Tunnel Started")
    def stop(self):
        self.server.stop()
        print("Tunnel Stopped")