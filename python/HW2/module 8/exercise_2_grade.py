#!/usr/bin/env python3

"""
Exercise 2: Letter Grade Calculator

Calculate and display a letter grade for a given numerical score.

Grading scale:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: 0-59
"""

score = 0

# Make sure the score is within the allowed range.
if score not in range(0, 101):
    print("Please enter a valid score 0-100")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
