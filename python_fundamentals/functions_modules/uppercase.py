#!/usr/bin/env python3

def uppercase(str):
    for index, letter in str:
        askey = ord(letter)

        charr = (askey - 32) if 97 <= askey <= 122 else letter
        print(charr, end="\n" if index == len(str) - 1 else "")
