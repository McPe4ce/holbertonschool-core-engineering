#!/usr/bin/activate

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        print("This isnt an integer")
