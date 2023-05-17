#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in range(len(matrix)):
        squared_row = []
        for index in range(len(matrix[row])):
            squared_element = matrix[row][index] ** 2
            squared_row.append(squared_element)
        result.append(squared_row)
    return result
