#!/usr/bin/python3
'''Write a class Square that defines a square by: (based on 4-square.py)'''


class Square:
    '''class Square'''

    def __init__(self, size=0, position=(0, 0)):
        ''' Private instance attribute: size'''
        self.__size = size
        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        '''returns the current square area'''
        return self.__size * self.__size

    @property
    def size(self):
        '''property'''
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        '''property setter'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
            if type(value) is not tuple:
                raise TypeError('position must be a tuple of 2 positive integers')
            elif len(value) != 2:
                raise TypeError('position must be a tuple of 2 positive integers')
            elif type(value[0]) != int or type(value[1]) != int:
                raise TypeError('position must be a tuple of 2 positive integers')
            elif value[0] < 0 or value[1] < 0:
                raise TypeError('position must be a tuple of 2 positive integers')

            else:
                self.__position = value

    def my_print(self):
        """function that print the square with the character #: """
        if self.__size == 0:
            print()
            return
        for l in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print('#', end="")
            print()
