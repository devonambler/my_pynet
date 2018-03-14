#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint
import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

#match = re.search(r'^Cisco (?P<model>\d.+) \S.+ processor.* with (?P<memory>\S.+) bytes.*', show_version, flags=re.M).groupdict()
match = re.search(r'^Cisco (?P<model>\d+).* with (?P<memory>\S.+) bytes.*', show_version, flags=re.M).groupdict()
if match:
    model_num = match.get('model')
    mem_num = match.get('memory')

    print('{:<20}: {:15}'.format('Cisco Model', model_num))
    print('{:<20}: {:15}'.format('Memory', mem_num))

