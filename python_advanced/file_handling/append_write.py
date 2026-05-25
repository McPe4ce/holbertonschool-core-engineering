#!/usr/bin/env python3
"""Module that appends a text to a file"""

def append_write(filename="", text=""):
    """'a' opens the file in append mode"""
    with open(f"{filename}", 'a') as f:
        return f.write(text)
