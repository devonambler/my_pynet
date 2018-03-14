#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint
import re

with open("show_version.txt") as f:
    show_version  = f.read()

## Find stuff with a one liner
#test = output.replace('\n', '')
#match = re.search(r'Cisco.+?Version (?P<os_ver>\S.+?),.+board ID (?P<ser_num>\S.+?)\s.+register is (?P<conf_reg>\S.+)', show_version).groupdict()
#os_ver, ser_num, conf_reg = match.get('os_ver'), match.get('ser_num'), match.get('conf_reg')

match = re.search(r'Cisco.+Version (\S.+),', show_version, flags=re.M)
if match:
    os_ver = match.group(1)

match = re.search(r'^Processor board ID (.*)\s*$', show_version, flags=re.M)
if match:
    ser_num = match.group(1)

match = re.search(r'^Configuration register is (.*)\s*$', show_version, flags=re.M)
if match:
    conf_reg = match.group(1)

print('OS Version: ' +  os_ver)
print('Serial Number: ' +  ser_num)
print('Config Register: ' + conf_reg)
