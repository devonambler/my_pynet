#!/usr/local/bin/python3

f = open("show_version.txt")

i = 0

while i <= 5:
    print("Hello")
    print("world")
    print(f.readline())
    i += 1
'''
f.seek(0)
i = 0

while i <= 5:
     line = f.readline()
     line = line.strip()
     print(line)
     i += 1
'''
