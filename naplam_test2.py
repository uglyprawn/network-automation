#!/usr/bin/python3
import json
from napalm import get_network_driver

f = open('hosts')
user = ''
pas = 'cisco'

for ip_add in f:
    print('Connecting to:' + str(ip_add).strip())

    driver = get_network_driver('ios')
    iosv_router = driver(ip_add, user, pas)
    iosv_router.open()
    bgp_neigh = iosv_router.get_bgp_neighbors()
    print(json.dumps(bgp_neigh, indent=4))
    iosv_router.close()

f.close()

