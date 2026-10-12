#!/usr/bin/env python3

"""
Exercise 1: Rectangle Area

Create a function named calculate_rectangle_area that calculates the area
of a rectangle.

The function accepts the length and width of the rectangle as arguments
and returns the calculated area by multiplying the length by the width.

Include a function docstring describing the function's purpose.
"""


def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


print(
    "Length: 10, Width: 11. The area of the rectangle is:",
    calculate_rectangle_area(10, 11),
)
print(
    "Length: 2, Width: 5. The area of the rectangle is:",
    calculate_rectangle_area(2, 5),
)
print(
    "Length: 4, Width: 100. The area of the rectangle is:",
    calculate_rectangle_area(4, 100),
)