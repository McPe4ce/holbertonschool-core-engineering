#!/usr/bin/env python3
"""Module defines the base of the Geometric behaviors"""


class BaseGeometry:
    """Class that defines the basic geometrics attributes"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value
