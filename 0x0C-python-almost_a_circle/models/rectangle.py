#!/usr/bin/python3
"""
This module implements a Rectangle object
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle implementation
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """initialization
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y
