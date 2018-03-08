#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint

houston_ips = [
        '192.168.200.99',
        '192.168.200.11',
        '192.168.200.12',
        '192.168.200.13',
        '192.168.200.14',
        '192.168.200.15',
        '192.168.200.16',
        '192.168.200.17',
        '192.168.200.18',
        '192.168.200.19',
        '192.168.200.20',
        '192.168.200.21',
        '192.168.200.45',
        '10.19.80.30',
        '10.19.80.39'
]

atlanta_ips = [
        '10.19.80.69',
        '10.19.80.31',
        '10.19.80.32',
        '10.19.80.33',
        '10.19.80.34',
        '10.19.80.35',
        '10.19.80.35',
        '10.19.80.37',
        '10.19.80.39',
        '192.168.200.19',
        '192.168.200.13'
]

chicago_ips = [
        '10.19.80.88',
        '10.19.80.31',
        '10.19.80.72',
        '10.19.80.33',
        '10.19.80.34',
        '10.19.80.35',
        '10.19.80.35',
        '10.19.80.37',
        '10.19.80.39',
        '192.168.200.19',
        '192.168.200.13'
]

houston_ip_set = set(houston_ips)
chicago_ip_set = set(chicago_ips)
atlanta_ip_set = set(atlanta_ips)

houston_atlanta_dupes = houston_ip_set.intersection(atlanta_ip_set)
print(houston_atlanta_dupes)
print()

all_dupe_ips = chicago_ip_set & houston_ip_set & atlanta_ip_set
print(all_dupe_ips)
print()

all_chicago = chicago_ip_set - houston_ip_set
all_chicago = all_chicago - atlanta_ip_set
print(all_chicago)

