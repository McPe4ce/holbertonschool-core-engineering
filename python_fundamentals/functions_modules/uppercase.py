#!/usr/bin/env python3

def uppercase(str):
    for letter in str:
        askey = ord(letter)

        if 97 <= askey <= 122:
            print(chr(askey - 32), end="")
        else:
            print("{}".format(letter), end="")
