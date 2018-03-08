#!/usr/local/bin/python3
from __future__ import print_function

try:
   #PY2
    ip_addr = raw_input('Please enter an IP address: ')
except NameError:
    # PY3
    ip_addr = input('Please enter an IP address: ')

octets = ip_addr.split('.')
octet1 = int(octets[0])
octet2 = int(octets[1])
octet3 = int(octets[2])
octet4 = int(octets[3])

print("{:^15}{:^15}{:^15}{:^15}".format('Octet1', 'Octet2', 'Octet3', 'Octet4'))
print('-' * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])),
                                        bin(int(octets[2])), bin(int(octets[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])),
                                        hex(int(octets[2])), hex(int(octets[3]))))
print('-' * 60)
