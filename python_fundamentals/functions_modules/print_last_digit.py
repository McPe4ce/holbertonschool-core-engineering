#!/usr/bin/env python3

def print_last_digit(number):

    el_last_digit = abs(number) % 10

    print("{}".format(el_last_digit), end="")
    return el_last_digit
