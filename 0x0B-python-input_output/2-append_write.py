#!/usr/bin/python3
"""Defines a function for appending text."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The file name to append text.
        text (str): The string to append to the file.
    Returns:
        The characters appended number.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
