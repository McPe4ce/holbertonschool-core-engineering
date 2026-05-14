#!/usr/bin/env python3
"""Module for the Square class that inherits from Rectangle"""

BaseGeometry = __import__('base_geometry').BaseGeometry
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherited, from the Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
