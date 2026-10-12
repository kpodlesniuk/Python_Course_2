#!/usr/bin/env python3

"""
Exercise 1: Square Numbers

Create a function that takes a list of numbers and returns a new list
containing the square of each number using the functional approach.
"""


def square(number):
    """Return the square of a number."""
    return number ** 2


def square_numbers(numbers):
    """Return a new list containing the square of each number."""
    return list(map(square, numbers))


print(square_numbers([-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))