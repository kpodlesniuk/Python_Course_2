#!/usr/bin/env python3

"""
Exercise 3: Factorial (optional)

Write a function that calculates the factorial of a number using
the functional approach.
"""

from functools import reduce


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def factorial(number):
    """Return the factorial of a number using the functional approach."""
    return reduce(multiply, range(1, number + 1), 1)


print(factorial(0))
print(factorial(10))