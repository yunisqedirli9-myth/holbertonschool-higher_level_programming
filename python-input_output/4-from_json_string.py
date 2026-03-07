#!/usr/bin/python3
"""Define a function that returns an object rep by json"""


# import json
import json


def from_json_string(my_str):
    """function that returns obj by json"""
    return json.loads(my_str)
