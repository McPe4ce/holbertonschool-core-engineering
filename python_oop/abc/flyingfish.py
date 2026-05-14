#!/usr/bin/env python3
"""Module that creates a FLyingFish class overriding bird and fish"""
from abc import abstractmethod


class Fish:

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:

    def fly(self):
        print("The bird is flyin")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):

    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
