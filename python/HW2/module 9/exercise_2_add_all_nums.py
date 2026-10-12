#!/usr/bin/env python3

"""
Exercise 2: Add All Numbers

Create a function named add_all_nums that accepts an arbitrary number
of arguments and returns their sum.

The function checks whether all provided arguments are numbers.
If any argument is not a number, it provides reasonable feedback.
"""


def add_all_nums(*args):
    """Calculate the sum of an arbitrary number of numeric arguments."""
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "Argument is not a number"
    return sum(args)


print("Result:", add_all_nums(1, 2, 3, 4, 5, 6, 7))
print("Result:", add_all_nums(1, "Kate", 3, 4))