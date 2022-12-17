#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Find a peak in the list of integers"""
    if list_of_integers == [] or list_of_integers is None:
        return None
    low = 0
    high = len(list_of_integers)
    middle = (((high - low) // 2) + low)
    if high == 1:
        return (list_of_integers[0])
    elif high == 2:
        return max(list_of_integers)
    if list_of_integers[middle] >= list_of_integers[middle -1] and\
            list_of_integers[middle] >= list_of_integers[middle +1]:
                return list_of_integers[middle]
    if middle > 0 and list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle:])
    elif middle > 0 and list_of_integers[middle] < list_of_integers[middle -1]:
        return find_peak(list_of_integers[:middle])
