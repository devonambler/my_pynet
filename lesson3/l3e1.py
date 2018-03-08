#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint

vlan_list = []

with open("show_vlan.txt") as f:
    vlan_file = f.readlines()

for line in vlan_file:
    line = line.split()
    line = line[:2]
    vlan_id = line[0]
    vlan_name = line[1]
    if vlan_id.isnumeric():
        vlan_list.append((vlan_id, vlan_name))
print()
print(vlan_list)
print()
