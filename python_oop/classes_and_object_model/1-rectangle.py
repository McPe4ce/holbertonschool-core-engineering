#!/usr/bin/env python3

class Rectangle:
    def __init__(self, width):
        self.__width = width

    @property
    def width(self):
        return self.width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value
    
    