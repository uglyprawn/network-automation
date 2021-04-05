#!/usr/bin/python3

from netmiko import ConnectHandler

ios_l2 = {
    'device_type': 'cisco_ios',
    'host': '1.1.2.1',
    'username': '',
    'password': 'cisco',
}

net_connect = ConnectHandler(**ios_l2)
output = net_connect.send_command('show ip int br')
print(output)

for n in range(2,10):
    print('Creating Vlan'+ str(n) + '\n')
    config_commands = ['vlan ' + str(n), 'name ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    #print(output)

print(net_connect.send_command('show vlan br'))