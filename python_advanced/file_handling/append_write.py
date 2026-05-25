#!/usr/bin/env python3


def append_write(filename="", text=""):
    with open(f"{filename}", 'a') as f:
        return f.write(text)
