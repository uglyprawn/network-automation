#!/usr/bin/python3

from netmiko import ConnectHandler

ios_l2_sw1= {
    'device_type': 'cisco_ios',
    'host': '1.1.2.1',
    'username': '',
    'password': 'cisco',
}

ios_l2_sw12= {
    'device_type': 'cisco_ios',
    'host': '1.1.2.2',
    'username': '',
    'password': 'cisco',
}

with open('cfg_vlans') as f:
    lines = f.read().splitlines()
print(lines)

all_devices =[ios_l2_sw1, ios_l2_sw12]

for n in all_devices:
    print('\n')
    print('\n')
    print('Configuring sw:' + str(n['host']) + '\n')
    net_connect = ConnectHandler(**n)
    output = net_connect.send_config_set(lines)
    print(output)

    print(net_connect.send_command('show vlan br'))