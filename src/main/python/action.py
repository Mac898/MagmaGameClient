import sys, json
import magmaGS
import python_hosts
from fbs_runtime.application_context.PyQt5 import ApplicationContext

class magmaGC_actions:
    def __init__(self, ui_main, main_logger, ssh_pass):
        #set imports as part of self
        self.uimain = ui_main
        self.ssh_tunnel = magmaGS.magmaGS(main_logger, ssh_pass)
        
        #read config
        self.actions_config_file = open(ApplicationContext().get_resource("actions_config.json"))
        self.actions_config = json.load(self.actions_config_file)
        print(self.actions_config)
        self.hosts_file = python_hosts.Hosts()

    #pass through logging function

    #begin actions
    def factorio_connect(self):
        factorio_port = self.actions_config['factorio']
        if self.uimain.factorioCheckBox.isChecked():
            print("Connecting Factorio!")
            self.ssh_tunnel.stop()
            self.ssh_tunnel.add_remote_bind(factorio_port, factorio_port)
            self.ssh_tunnel.start()
        else:
            print("Disconnecting Factorio!")
            self.ssh_tunnel.stop()
            self.ssh_tunnel.remove_remote_bind(factorio_port, factorio_port)
            self.ssh_tunnel.start()

    def minecraft_connect(self):
        mc_auth_host_names = ['authserver.mojang.com', 'launchermeta.mojang.com']
        minecraft_hosts = python_hosts.HostsEntry(entry_type='ipv4', address='127.0.0.1', names= mc_auth_host_names)
        minecraft_port = self.actions_config['minecraft']
        minecraft_auth_port = self.actions_config['minecraft_auth']
        if self.uimain.minecraftCheckBox.isChecked():
            print("Connecting Minecraft!")
            self.hosts_file.add([minecraft_hosts])
            self.hosts_file.write()
            self.ssh_tunnel.stop()
            self.ssh_tunnel.add_remote_bind(minecraft_port,minecraft_port)
            self.ssh_tunnel.add_remote_bind("443", minecraft_auth_port)
            self.ssh_tunnel.start()
        else:
            print("Disconnecting Minecraft!")
            self.hosts_file.remove_all_matching(name=mc_auth_host_names[0])
            self.hosts_file.remove_all_matching(name=mc_auth_host_names[1])
            self.hosts_file.write()
            self.ssh_tunnel.stop()
            self.ssh_tunnel.remove_remote_bind(minecraft_port, minecraft_port)
            self.ssh_tunnel.remove_remote_bind("443", minecraft_auth_port)
            self.ssh_tunnel.start()
    def custom_connect(self, num, port, custom_checkbox_list):
        custom_port = port
        list_num = num - 1
        if custom_checkbox_list[list_num].isChecked():
            print("Connecting Custom forward: "+str(num))
            self.ssh_tunnel.stop()
            self.ssh_tunnel.add_remote_bind(custom_port, custom_port)
            self.ssh_tunnel.start()
        else:
            print("Disconnecting Custom forward: "+str(num))
            self.ssh_tunnel.stop()
            self.ssh_tunnel.remove_remote_bind(custom_port, custom_port)
            self.ssh_tunnel.start()