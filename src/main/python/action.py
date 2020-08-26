import sys, json
import magmaGS

class magmaGC_actions:
    def __init__(self, ui_main, main_logger):
        #set imports as part of self
        self.uimain = ui_main
        self.ssh_tunnel = magmaGS.magmaGS(main_logger)
        
        #read config
        self.actions_config_file = open("actions_config.json")
        self.actions_config = json.load(self.actions_config_file)
        print(self.actions_config)

    #pass through logging function

    #begin actions
    def factorio_connect(self):
        factorio_port = self.actions_config['factorio']
        if self.uimain.factorioCheckBox.isChecked():
            print("Connecting Factorio!")
            
            self.ssh_tunnel.stop()
            self.ssh_tunnel.add_remote_bind(factorio_port)
            self.ssh_tunnel.start()
        else:
            print("Disconnecting Factorio!")
            self.ssh_tunnel.stop()
            self.ssh_tunnel.remove_remote_bind(factorio_port)
            self.ssh_tunnel.start()

    def minecraft_connect(self):
        minecraft_port = self.actions_config['minecraft']
        if self.uimain.factorioCheckBox.isChecked():
            print("Connecting Factorio!")
            
            self.ssh_tunnel.stop()
            self.ssh_tunnel.add_remote_bind(minecraft_port)
            self.ssh_tunnel.start()
        else:
            print("Disconnecting Factorio!")
            self.ssh_tunnel.stop()
            self.ssh_tunnel.remove_remote_bind(minecraft_port)
            self.ssh_tunnel.start()


