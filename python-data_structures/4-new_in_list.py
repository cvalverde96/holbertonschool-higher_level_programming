#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    new_list = my_list[:]
    if idx >= 0 and len(my_list) > 0:
        new_list[idx] = new_element
    return new_list
