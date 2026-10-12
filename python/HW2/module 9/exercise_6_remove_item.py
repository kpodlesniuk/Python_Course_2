#!/usr/bin/env python3

"""
Exercise 6: Remove Item

Create a function named remove_item that removes an item from a given list.

The function accepts a list and an item as arguments and returns the list
with the specified item removed.
"""


def remove_item(items, item):
    """Remove an item from a list and return the list."""
    items.remove(item)
    return items


numbers = [1, 2, 3, 4, 5, 6]
colors = ["red", "green", "blue", "yellow", "black"]

print(
    "Remove 5 from the numbers list:",
    remove_item(numbers, 5),
)
print(
    "Remove black from the colors list:",
    remove_item(colors, "black"),
)