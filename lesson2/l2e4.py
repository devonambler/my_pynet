#!/usr/local/bin/python3
from __future__ import print_function, unicode_literals
from pprint import pprint

with open("show_ip_int_brief.txt") as f:
    output = f.readlines()

line = output[5].split()

mytuple = (line[0], line[1])

print(mytuple)
