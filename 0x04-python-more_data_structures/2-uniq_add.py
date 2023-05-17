#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = set()
    sum_unique = 0
    for number in my_list:
        if number not in set_list:
            sum_unique += number
            set_list.add(number)
    return (sum_unique)
