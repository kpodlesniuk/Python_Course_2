#!/usr/bin/env python3

"""
Exercise 4: Reverse List

Create a function named reverse_list that reverses a given list.

The function accepts a list as an argument and returns the elements
in reverse order using a loop.
"""


def reverse_list(array):
    """Return the elements of a list in reverse order using a loop."""
    reversed_array = []
    for item in array:
        reversed_array.insert(0, item)
    return reversed_array


print(
    'Reversed order for the elements in the list [1, 2, 3]:',
    reverse_list([1, 2, 3]),
)
print(
    "Reversed order for the elements in the list ['A', 'B', 'C']:",
    reverse_list(["A", "B", "C"]),
)