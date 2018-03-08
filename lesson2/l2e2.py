#!/usr/local/bin/python3
from __future__ import print_function

my_list = []
my_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]
my_list.append("10.10.10.1")
my_list.extend(["172.17.0.1", "172.17.0.2"])
my_list = my_list + ["192.168.1.6", "192.168.1.7"]
print(my_list)

print(my_list[0])
print(my_list[-1])

my_list.pop(0)
my_list.pop()

my_list[0] = "2.2.2.2"

print("\nFirst New List Element:\n" + my_list[0])
