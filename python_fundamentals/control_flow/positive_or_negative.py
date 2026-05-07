#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)

if number > 0:
    print("{} is positive")
elif number == 0:
    print("{} is zero")
else:
    print("{} is negative")
