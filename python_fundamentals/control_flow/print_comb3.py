#!/usr/bin/env python3

for index in range(9):
    for dedex in range(index + 1, 10):
        if index == 8 and dedex == 9:
            print("{}{}".format(index, dedex))
        else:
            print("{}{}".format(index, dedex), end=", ")
