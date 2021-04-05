#!/usr/bin/python3
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('1.1.2.2', '', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_bgp_neighbors()
print(json.dumps(ios_output, indent=4))

#ios_output = iosvl2.ping('10.1.1.1')
#print(json.dumps(ios_output, indent=4))

#ios_output = iosvl2.get_mac_address_table()
#print(json.dumps(ios_output, indent=4))

#ios_output = iosvl2.get_interfaces()
#print(json.dumps(ios_output, indent=4))

#ios_output = iosvl2.get_interfaces_counters()
#print(json.dumps(ios_output, indent=4))

iosvl2.close()