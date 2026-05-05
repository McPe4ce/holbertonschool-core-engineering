#!/usr/bin/env python3

def uppercase(str):
    for letter in str:
        askey = ord(letter)
        if 97 <= askey <= 122:
            askey -= 32
        print("{}".format(chr(askey)), end="")
    print()
