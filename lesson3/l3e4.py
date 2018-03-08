#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint

arp_table = [('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')]

for arps in arp_table:
    mac_addr = arps[1]
    mac_addr = mac_addr.split(sep=".")
    mac_addr = "".join(mac_addr)
    mac_addr = mac_addr.upper()
   ''' 
    # my first attempt at processing
    # the addresses two digits at a time
    mac_list = list(mac_addr)
    oct1 = mac_list[0] + mac_list[1]
    oct2 = mac_list[2] + mac_list[3]
    oct3 = mac_list[4] + mac_list[5]
    oct4 = mac_list[6] + mac_list[7]
    oct5 = mac_list[8] + mac_list[9]
    oct6 = mac_list[10] + mac_list[11]
    print("{}:{}:{}:{}:{}:{}".format(oct1,oct2,oct3,oct4,oct5,oct6))
    '''
    # Process two hex digits at a time
    new_mac = []
    while len(mac_addr) > 0:
        entry = mac_addr[:2]
        mac_addr = mac_addr[2:]
        new_mac.append(entry)

    # Reunite MAC address using a colon
    new_mac = ":".join(new_mac)
    print(new_mac)
print()
