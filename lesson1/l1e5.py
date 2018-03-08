#!/usr/local/bin/python3
from __future__ import print_function

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1_list = mac1.split()
mac2_list = mac2.split()
mac3_list = mac3.split()
print('{:>20}{:>20}'.format('IP ADDR', 'MAC ADDRESS'))
print('{:>20}{:>20}'.format('-' * 19, '-' * 19))
print('{:>20}{:>20}'.format(mac1_list[1], mac1_list[3]))
print('{:>20}{:>20}'.format(mac2_list[1], mac2_list[3]))
print('{:>20}{:>20}'.format(mac3_list[1], mac3_list[3]))
