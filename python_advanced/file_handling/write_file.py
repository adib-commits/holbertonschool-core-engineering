#!/usr/bin/env python3

def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return number of chars"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
