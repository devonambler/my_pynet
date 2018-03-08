#!/usr/local/bin/python3

my_dict = {}
my_list = []

###try:
###    my_list[0]
###    my_dict['ip_addr']
###except (KeyError, IndexError):
###    print("Handled multiple potention exceptions")

try:
    my_list[0]
    my_dict['ip_addr']
except KeyError:
    print("handled KeyError")
except IndexError:
    print("handled IndexError")
finally:
    print("finally always executes")


#try:
#except Exception:
