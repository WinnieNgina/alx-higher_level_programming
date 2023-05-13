#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for index in range(len(matrix[row])):
            print("{:d}".format(matrix[row][index]), end="")
            if index != (len(matrix[row]) - 1):
                print(" ", end="")
        print("")
