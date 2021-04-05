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

all_devices =[ios_l2_sw1, ios_l2_sw12]

for m in all_devices:
    net_connect = ConnectHandler(**m)
    output = net_connect.send_command('show vlan br')
    print("configuring sw: " + m['host'])
    print(output)

    for n in range(2,5):
        print('Creating Vlan'+ str(n) + '\n')
        #print('Deleteing vlan' + str(n) + '\n')
    
        config_commands = ['vlan ' + str(n), 'name Vlan ' + str(n)]
        #config_commands = ['no vlan ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        #print(output)

    print(net_connect.send_command('show vlan br'))
