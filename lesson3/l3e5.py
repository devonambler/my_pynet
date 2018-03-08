#!/usr/local/bin/python3
from __future__ import unicode_literals, print_function
from pprint import pprint
import os

# Toggle to use windows
WINDOWS = False

ip_list = []

base_cmd_linux = 'ping -c 2 '
base_cmd_windows = 'ping -n 2 '
base_ip = '10.10.100.'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

for myip in range(1,255):
    new_ip = base_ip + str(myip)
    ip_list.append(new_ip)
    #ip_list = ip_list + [base_ip + str(myip)]

for i, ip_addr in enumerate(ip_list):
    # print(str(i) + " ---> " + ip_addr)
    # Cleaner?
    print("{} ---> {}".format(i, ip_addr))
new_list = ip_list[2:6]

test_list = ["192.168.0.31", "192.168.0.33", "192.168.0.34"]

for ip in test_list:
    print("IP Addr: ", ip)
    return_code = os.system(base_cmd + ip)
    print('-' * 80)
print('-' * 80)
print()

