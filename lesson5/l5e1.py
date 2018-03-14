#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint

def ssh_conn(ip_addr, username, password, device_type='cisco_ios'):
    print('{:>20}{:>20}{:>20}{:>20}'.format('IP ADDRESS', 'USERNAME', 'PASSWORD', 'DEVICE TYPE'))
    print('{:>20}{:>20}{:>20}{:>20}'.format(ip_addr, username, password, device_type))
    print()

ssh_conn('192.168.1.1', 'admin', 'bombs')

ssh_conn(username='devon', ip_addr='10.10.0.1', password='procurve')

ssh_conn('10.12.13.1', password='superday', username='root') 

ssh_conn('10.12.13.1', password='superday', username='root', device_type='my device')

my_dict = {
        'ip_addr': '10.19.80.1',
        'username': 'badmofo',
        'password': 'noshit',
        'device_type': 'juniper'
}

ssh_conn(**my_dict)
