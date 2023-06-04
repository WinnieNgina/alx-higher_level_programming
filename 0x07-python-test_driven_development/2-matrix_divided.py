#!/usr/bin/python3
def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                "integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            divided_num = round(num / div, 2)
            new_row.append(divided_num)
        new_matrix.append(new_row)

    return new_matrix
