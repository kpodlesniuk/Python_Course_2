#!/usr/bin/env python3

"""
Exercise 3: Check Season

Create a function named check_season that determines the season
based on a given month.

The function accepts a month as an argument and returns the corresponding
season: Autumn, Winter, Spring, or Summer.
"""


def check_season(month):
    """Return the season based on the given month."""
    if month in ("September", "October", "November"):
        return "Autumn"
    elif month in ("December", "January", "February"):
        return "Winter"
    elif month in ("March", "April", "May"):
        return "Spring"
    elif month in ("June", "July", "August"):
        return "Summer"
    else:
        return "Invalid month"


print("Result for December is:", check_season("December"))
print("Result for March is:", check_season("March"))
print("Result for August is:", check_season("August"))
print("Result for October is:", check_season("October"))
print("Result for Potato is:", check_season("Potato"))
