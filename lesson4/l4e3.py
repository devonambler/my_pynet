#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint



with open("show_version.txt") as f:
    output = f.read()

test = output.replace('\n', '')
match = re.search(r'Cisco.+?Version (?P<os_ver>\S.+?),.+board ID (?P<ser_num>\S.+?)\s.+register is (?P<conf_reg>\S.+)', test).groupdict()
match.get('os_ver')
