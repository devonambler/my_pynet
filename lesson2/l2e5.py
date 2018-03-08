#!/usr/local/bin/python3
from __future__ import print_function, unicode_literals
from pprint import pprint

with open("show_ip_bgp_summ.txt") as f:
    summ = f.readlines()

mytuple = (summ[0], summ[-1])

localas = mytuple[0].split()
localas = localas[-1]

peer = mytuple[1].split()
peer = peer[0]

print("Local AS = " + localas)
print("Peer = " + peer)
