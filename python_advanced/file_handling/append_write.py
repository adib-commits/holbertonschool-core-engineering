#!/usr/bin/env python3

def append_write(filename="", text=""):
    """Append a string at the end of a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
