#!/usr/bin/python3
"""
Function returns a list of integers representing Pascal's triangle
or returns an empty list if n <= 0
"""


def pascal_triangle(n):
    """
    We initialize the triangle with the first list [1].
    For each subsequent list, we iterate from index 1 to i-1,
    excluding the first and last element.
    The value of each element in the current list is calculated by adding
    the corresponding element and the previous element from the previous list.
    We append the calculated elements to the list.
    Args:
        n: determines the number of lists created
    """
    if n <= 0:
        return []

    triangle = [[1]]  # first list
    for i in range(1, n):
        # we start from 1 because we have already initialized the first row
        List = [1]  # In each list, List[0] = 1

        for j in range(1, i):  # j represents the index of the current list
            # Calculate each element in the list based on the previous list
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            List.append(element)  # Appends the calculated element to the list

        List.append(1)  # Appends 1 at the end of the list List[-1]
        triangle.append(List)  # Add the list to the triangle

    return triangle
