#!/usr/bin/python3
"""Define function that returns JSON rep of an object"""


import json


def to_json_string(my_obj):
    """function that returns JSON rep"""
    return json.dumps(my_obj)
