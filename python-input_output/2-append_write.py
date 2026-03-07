#!/usr/bin/python3
"""Define function to append string to file"""


def append_write(filename="", text=""):
    """function to append string to file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
