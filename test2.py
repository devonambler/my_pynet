from __future__ import print_function, unicode_literals

ip_addr = '192.168.1.1'
octets = ip_addr.split('.')

print('\n')
print("-" * 80)
print("{:10}{:10}{:10}{:10}".format(*octets))
#print("{:10}{:10}{:10}{:10}".format(octets[0], octets[1], octets[2], octets[3]))
print("-" * 80)
print('\n')
