#!/usr/bin/env python3
"""Module that creates a dragon class using mixin"""


class SwimMixin:

    def swim(self):
        print("The creature swims!")


class FlyMixin:

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):

    def roar(self):
        print("The dragon roars!")
