#!/usr/local/bin/python3
from __future__ import print_function
from pprint import pprint

with open("show_arp.txt") as f:
    output = f.readlines()

pprint(output)

output = output[1:]

output.sort()

first3 = output[:3]

first3 = '\n'.join(first3)

with open("arp_entries.txt", mode="w") as f:
    f.write(first3)
