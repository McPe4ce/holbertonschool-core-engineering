#!/usr/bin/env python3
"""Module that writes in a file and returns the number of chars in it"""


def write_file(filename="", text=""):
    """w+ truncates the file and updates it"""
    with open(f"{filename}", 'w+', encoding="utf-8") as f:
        return f.write(text)
