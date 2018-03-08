#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint

with open("show_arp.txt") as f:
    show_arp = f.readlines()

gateway, arista  = (False, False)

print()

for arps in show_arp:
    line = arps.split()
    ip_addr = line[1]
    mac_addr = line[3]
    if ip_addr == "10.220.88.1":
        print("Default gateway IP/Mac is {}    :    {}".format(ip_addr, mac_addr))
        gateway = True
    if ip_addr == "10.220.88.30":
        print("Arista3 IP/Mac is: {}   :   {}".format(ip_addr, mac_addr))
        arista = True
    if gateway & arista:
        print("Exiting...")
        break
