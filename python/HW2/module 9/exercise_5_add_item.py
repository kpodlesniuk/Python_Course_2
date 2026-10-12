#!/usr/bin/env python3

"""
Exercise 5: Add Item

Create a function named add_item that adds an item to a given list.

The function accepts a list and an item as arguments and returns the list
with the item added at the end.
"""


def add_item(items, item):
    """Add an item to the end of a list and return the list."""
    items.append(item)
    return items


numbers = [1, 2, 3]
colors = ["red", "green", "blue"]

print(
    "Add 5 to the numbers list:",
    add_item(numbers, 5),
)
print(
    "Add black to the colors list:",
    add_item(colors, "black"),
)