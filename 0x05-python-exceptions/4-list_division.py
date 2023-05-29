#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            div_results = a/b
        except TypeError:
            print("wrong type")
            div_results = 0
        except ZeroDivisionError:
            print("division by 0")
            div_results = 0
        except IndexError:
            print("out of range")
            div_results = 0
        finally:
            results.append(div_results)
    return results
