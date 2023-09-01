#!/usr/bin/python3
""" Module to find peak """
def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers.'''
    def binary_search_peak(arr, left, right):
        '''Recurcise function to find peak'''
        if left == right:
            return arr[left]
        mid = (left + right) // 2
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return binary_search_peak(arr, left, mid - 1)
        else:
            return binary_search_peak(arr, mid + 1, right)
    if not list_of_integers:
        return None
    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)