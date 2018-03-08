#!/usr/local/bin/python3
from __future__ import print_function

'''
##Old Way
f = open("show_version.txt")
output = f.read()

print(output)

f.close()
'''

with open ("show_version.txt") as f:
    output = f.readlines()
    print(output)
    print(type(output))
