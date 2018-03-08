#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint

network_device = {
        'ip_addr': '192.168.1.1', 
        'vendor': 'cisco', 
        'username': 'bob', 
        'password': 'bombs'
}

print(network_device['ip_addr'])

print()

if network_device.get('vendor').lower() == 'cisco':
    network_device['platform'] = 'ios'
elif net_device.get('vendor').lower() == 'juniper':
    network_device['platform'] = 'junos'

bgp_fields = {'bgp_as': '192.168.2.1', 'peer_as': '192.168.3.1', 'peer_ip': '192.168.4.1'}

network_device.update(bgp_fields)

for key in network_device.keys():
    print('{:>15}'.format(key))

print()

for key, value in network_device.items():
    print('{key:>15} ---> {value:>15}'.format(key=key, value=value))

