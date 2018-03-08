#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint

with open("show_lldp_neighbors_detail.txt") as f:
    #lldp_out = f.readlines()
    lldp_out = f.read()

sysname, portname = (None, None)

for lines in lldp_out.splitlines():
    '''
    if len(myline) >= 3:
        if myline[0] == "System" and myline[1] == "Name:":
            sysname = myline[2]
        if myline[0] == "Port" and myline[1] == "id:":
            portname = myline[2]
    '''
    if 'System Name: ' in lines:
        _, sysname = lines.split('System Name: ')
    elif 'Port id: ' in lines:
        _, portname = lines.split('Port id: ')
    
    if sysname and portname:
        break

print("{:<20}{:<20}".format("System Name","Port Name"))
print("{:<20}{:<20}".format("-"*19, "-"*19))
print("{:<20}{:<20}".format(sysname, portname))

