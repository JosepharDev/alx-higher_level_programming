#!/usr/bin/python3
"""Defines a function converting string-to-JSON."""
import json


def to_json_string(my_obj):
    """Return the representation of a string in JSON."""
    return json.dumps(my_obj)
