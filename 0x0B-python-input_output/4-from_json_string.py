#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function converting JSON to string."""
import json


def from_json_string(my_str):
    """Return the JSON string object representation."""
    return json.loads(my_str)
