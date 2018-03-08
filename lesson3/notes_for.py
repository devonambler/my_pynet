#!/usr/local/bin/python3

ip_address_list = ['192.168.1.1', '10.1.1.1', '10.10.20.30', '172.16.31.254']
'''
for ip in ip_address_list:
    print(ip)

for my_var in enumerate(ip_address_list):
    print(my_var)

for i, ip_addr in enumerate(ip_address_list):
    print(i)
    print(ip_addr)
    print('-' * 30)

for ip in ip_address_list:
    print(ip)
    if ip == '10.10.20.30':
        break

for ip in ip_address_list:
   print("hello")
   if ip == '10.10.20.30':
        continue
    print(ip)

ip_list2 = ['8.8.8.8', '8.8.4.4']
for ip in ip_address_list:
    for ip2 in ip_list2:
        print(ip)
        print(ip2)

for my_var in range(10):
    print(my_var)        

for my_var in range(1, 17):
    print(my_var)
'''
if '192.168.1.1' in ip_address_list:
    print("it is")
