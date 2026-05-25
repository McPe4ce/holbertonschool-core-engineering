#!/usr/bin/env python3
"""Function that reads the content of a file in UTF-8"""


def read_file(filename=""):
    with open(f"{filename}", encoding="utf-8") as f:
        reader = f.read()
