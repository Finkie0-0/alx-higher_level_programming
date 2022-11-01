#!/usr/bin/python3
'''Write a class Square that defines a square by: (based on 3-square.py)'''


class Square:
    '''class Square'''

    def __init__(self, size=0):
        ''' Private instance attribute: size'''
        self.__size = size

    def area(self):
        '''returns the current square area'''
        return self.__size * self.__size

    @property
    def size(self):
        '''property'''
        return self.__size

    @size.setter
    def size(self, value):
        '''property setter'''
        if type(value) is not int:
                raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
