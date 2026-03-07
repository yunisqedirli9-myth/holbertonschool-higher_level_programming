#!/usr/bin/python3
"""Define a function to write a string to a file"""


def write_file(filename="", text=""):
    """function to write string"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
