#!/usr/bin/env python3
def no_c(my_string):
    my_new_string = my_string.translate({ord(i): '' for i in 'cC'})
    return (my_new_string)
