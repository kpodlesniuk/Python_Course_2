#!/usr/bin/env python3

"""
Exercise 5: Average Score (optional)

Given a list of students and their marks as tuples, write a function
that calculates and returns the average score.
"""

from functools import reduce


def get_score(student):
    """Return the score from a student tuple."""
    return student[1]


def adding(a, b):
    """Return the sum of two numbers."""
    return a + b


def calculate_average_score(scores):
    """Calculate and return the average score."""
    only_scores = list(map(get_score, scores))
    total_score = reduce(adding, only_scores)
    average_score = total_score / len(only_scores)

    return average_score


scores = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
]

print(calculate_average_score(scores))