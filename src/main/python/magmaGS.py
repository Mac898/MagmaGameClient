from sshtunnel import SSHTunnelForwarder, create_logger as SSHTF_create_logger
import json

class magmaGS:
    def __init__(self, main_logger):
        self.main_logger = main_logger
        #define settings from config
        self.remote_list = [("127.0.0.1",6969)]
        self.creds_file = open("pass.credential", "r")
        self.creds_pass = self.creds_file.readline()
        self.ssh_config_file = open("ssh_config.json")
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
            local_bind_addresses=self.remote_list
        )

    #add remote bind
    def add_remote_bind(self, bind_port):
        to_add = ("127.0.0.1", int(bind_port))
        self.remote_list.append(to_add)
        print("Adding remote bind: "+str(to_add))
        
    #remove remote bind
    def remove_remote_bind(self, bind_port):
        to_remove = ("127.0.0.1", int(bind_port))
        print("Removing remote bind: "+str(to_remove))
        try:
            self.remote_list.remove(to_remove)
        except ValueError:
            print("Tried to remove bind from list before addition")

    #control tunnel
    def start(self):
        self.server.start()
        print("Tunnel Started")
    def stop(self):
        self.server.stop()
        print("Tunnel Stopped")