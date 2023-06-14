#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    high = my_list[0]
    for i in range(1, len(my_list)):
        if high < my_list[i]:
            high = my_list[i]
        else:
            continue
    return high
