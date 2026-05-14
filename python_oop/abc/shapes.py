#!/usr/bin/activate
"""Module that creates ABC Shape with its subclasses Circle and Rectangle
and uses duck typing to call them"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(name):
    # Duck typing: call the methods directly, no isinstance/type checks.
    area = name.area()
    perimeter = name.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
