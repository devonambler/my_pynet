#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint
import random
import re

def normalize_mac(mac_address):
    if re.match(r'(\S\S\S\S)\.(\S\S\S\S)\.(\S\S\S\S)', mac_address):
        fix_mac = mac_address.split(sep='.')
    
    elif re.match(r'\S\S-\S\S-\S\S-\S\S-\S\S-\S\S', mac_address):
        fix_mac = mac_address.split(sep='-')
    
    elif re.match(r'\S:\S:\S:\S:\S:\S', mac_address):
        fix_mac = mac_address.split(sep=':')
        count = 0
        for i in fix_mac:
            fix_mac[count] = '0' + i
            count = count + 1
    else:
        raise ValueError(mac_address + ': Is an invalid input')
    
    fix_mac = "".join(fix_mac)
    fix_mac = fix_mac.upper()
    new_mac = []
    
    while len(fix_mac) >= 2:
        entry = fix_mac[:2]
        fix_mac = fix_mac[2:]
        new_mac.append(entry)
    new_mac = ":".join(new_mac)
    
    print('Normalizing: ' + mac_address + ' to: '+  new_mac)
    print()
    
mac_test1 = '00C0.aaaC.cbbb'
mac_test2 = '01-02-aE-aE-bb-bb'
mac_test4 = ':b:c:d:e:f'
mac_test3 = 'a:b:c:d:e:f'

normalize_mac(mac_test1)
normalize_mac(mac_test2)
normalize_mac(mac_test3)
normalize_mac(mac_test4)
