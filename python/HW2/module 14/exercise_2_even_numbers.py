#!/usr/bin/env python3

"""
Exercise 2: Even Numbers

Create a function that takes a list of numbers and returns a new list
containing only the even numbers using the functional approach.
"""


def is_even(number):
    """Return True if the number is even."""
    return number % 2 == 0


def even_numbers(numbers):
    """Return a new list containing only the even numbers."""
    return list(filter(is_even, numbers))


print(even_numbers([-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))