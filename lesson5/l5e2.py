#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint
import random

def random_ip(base_network='10.10.10.'):
    print('Base Network: {}'.format(base_network))
    print()
    return_ip = base_network + str(random.randint(1,254))
    print('Random IP: {}'.format(return_ip))

random_ip('192.168.3.')
