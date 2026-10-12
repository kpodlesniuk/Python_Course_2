#!/usr/bin/env python3

"""
Exercise 1: Temperature Checker

Write a Python program that checks the temperature and prints a message
based on its value.

- Above 27°C: print "It's a hot day."
- 27°C or below: print "It's not a hot day."

Test the program with at least three values: one above 27, exactly 27,
and one below 27.
"""

temperatures = [30, 27, 20]

for temperature in temperatures:
    if temperature > 27:
        print("It's a hot day.")
    else:
        print("It's not a hot day.")
