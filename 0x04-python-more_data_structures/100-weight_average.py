#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    total_scores = 0
    total_weight = 0
    for score, weight in my_list:
        total_scores += weight * score
        total_weight += weight
    return (total_scores/total_weight)
