#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    new_list = my_list[:]
    if 0 <= idx < len(my_list):
        new_list[idx] = new_element
    return new_list
