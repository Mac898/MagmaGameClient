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
        #hosts
        minecraft_hosts_entrys = [python_hosts.HostsEntry(entry_type='ipv4', address='127.0.0.2', names='authserver.mojang.com'),python_hosts.HostsEntry(entry_type='ipv4', address='127.0.0.3', names='sessionserver.mojang.com'),
        python_hosts.HostsEntry(entry_type='ipv4', address='127.0.0.4', names='launchermeta.mojang.com'), python_hosts.HostsEntry(entry_type='ipv4', address='127.0.0.5', names='accounts.mojang.com'),
        python_hosts.HostsEntry(entry_type='ipv4', address='127.0.0.6', names='meta.multimc.org')]
        #get ports
        minecraft_port = self.actions_config['minecraft']
        minecraft_modded_port = self.actions_config['minecraft_modded']
        minecraft_authserver_port = self.actions_config['minecraft_auth_authserver']
        minecraft_sessionserver_port = self.actions_config['minecraft_auth_sessionserver']
        minecraft_launchermeta_port = self.actions_config['minecraft_auth_launchermeta']
        minecraft_accounts_port = self.actions_config['minecraft_auth_accounts']
        minecraft_multimeta_port = self.actions_config['minecraft_auth_multimc']
        #begin actual stuff
        if self.uimain.minecraftCheckBox.isChecked():
            print("Connecting Minecraft!")
            self.hosts_file.add(minecraft_hosts_entrys)
            self.hosts_file.write()
            self.ssh_tunnel.stop()
            self.ssh_tunnel.add_remote_bind(minecraft_port,minecraft_port)
            self.ssh_tunnel.add_remote_bind(minecraft_modded_port,minecraft_modded_port)
            self.ssh_tunnel.add_remote_bind("443", minecraft_authserver_port, ip="127.0.0.2")
            self.ssh_tunnel.add_remote_bind("443", minecraft_sessionserver_port, ip="127.0.0.3")
            self.ssh_tunnel.add_remote_bind("443", minecraft_launchermeta_port, ip="127.0.0.4")
            self.ssh_tunnel.add_remote_bind("443", minecraft_accounts_port, ip="127.0.0.5")
            self.ssh_tunnel.add_remote_bind("443", minecraft_multimeta_port, ip="127.0.0.6")
            self.ssh_tunnel.start()
        else:
            print("Disconnecting Minecraft!")
            self.hosts_file.remove_all_matching(name="authserver.mojang.com")
            self.hosts_file.remove_all_matching(name="sessionserver.mojang.com")
            self.hosts_file.remove_all_matching(name="launchermeta.mojang.com")
            self.hosts_file.remove_all_matching(name="accounts.mojang.com")
            self.hosts_file.remove_all_matching(name="meta.multimc.org")
            self.hosts_file.write()
            self.ssh_tunnel.stop()
            self.ssh_tunnel.remove_remote_bind(minecraft_port, minecraft_port)
            self.ssh_tunnel.remove_remote_bind(minecraft_modded_port, minecraft_modded_port)
            self.ssh_tunnel.remove_remote_bind("443", minecraft_authserver_port)
            self.ssh_tunnel.remove_remote_bind("443", minecraft_authserver_port, ip="127.0.0.2")
            self.ssh_tunnel.remove_remote_bind("443", minecraft_sessionserver_port, ip="127.0.0.3")
            self.ssh_tunnel.remove_remote_bind("443", minecraft_launchermeta_port, ip="127.0.0.4")
            self.ssh_tunnel.remove_remote_bind("443", minecraft_accounts_port, ip="127.0.0.5")
            self.ssh_tunnel.remove_remote_bind("443", minecraft_multimeta_port, ip="127.0.0.6")
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