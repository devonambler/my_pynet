#!/usr/local/bin/python3

# Allow Python2 to run Python3 happily  
from __future__ import print_function, unicode_literals

my_str = 'whatev'
print(my_str)

# whatefer our comments is

'''
This is a multiline comment
Line
'''
print("Hello world")
ip_addr1 = '8.8.8.8'
print(ip_addr1)

try: 
    # Python3
    ip_addr = input("Enter an IP Address: ")
except NameError:
    # Python2
    ip_addr = raw_input("Enter an IP Address: ")

print(ip_addr)
