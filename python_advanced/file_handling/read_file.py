#!/usr/bin/env python3

def read_file(filename=""):
    with open(f"{filename}", encoding="utf-8") as f:
        reader = f.read()
