#!/usr/local/bin/python3
from __future__ import print_function

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()
splits = show_version.split()
serial_num = splits[2]
model_num = splits[1]

print()
cisco_check = 'cisco' in show_version.lower()
print('\nCheck if \'Cisco\' is contained in the model string (ignore capitalization): {}'.format(cisco_check))

print('\nSplit the string and extract the model and serial_number from it.')
print('Serial Number = ' + serial_num)
print('\nModel Number = ' + model_num)
model_881 = '881' in model_num
print('\nCheck if \'881\' is in the model string: {}'.format(model_881))
print()
