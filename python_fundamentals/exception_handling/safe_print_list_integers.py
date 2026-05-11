#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for indexor in range(x):
            if isinstance(my_list[indexor], int):
                print(my_list[indexor], end=" ")
                counter += 1
        print()
    except (TypeError, IndexError):
        pass
    return counter
