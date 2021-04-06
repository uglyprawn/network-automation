#!/usr/bin/python3

import json
from pyntc import ntc_device as NTC

iosvl2 = NTC(host='1.1.2.1', username='', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

#iosvl2.config('hostname sw1')

#ios_run = iosvl2.running_config
#print(ios_run)

#bkcfg = open('switch_cfg', 'w')
#bkcfg.write(ios_run)
#bkcfg.close()

ios_run = iosvl2.backup_running_config('switch_cfg')
iosvl2.close()
