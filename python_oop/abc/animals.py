#!/usr/bin/enbv python3
"""Module that defines the ABC ANimal and its inheritors"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        ...


class Dog(Animal):

    def sound(self):
        return "Bark"


class Cat(Animal):

    def sound(self):
        return "Meow"
