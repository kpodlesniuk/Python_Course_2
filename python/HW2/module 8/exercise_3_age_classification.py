#!/usr/bin/env python3

"""
Exercise 3: Age Classification

Ask the user for their age and classify it into one of the following categories:

- Infant: 0-2 years old
- Child: 3-12 years old
- Teenager: 13-19 years old
- Adult: 20-64 years old
- Senior: 65 years old and older

Display the corresponding age classification.
"""

age = int(input("Please enter your age: "))

# Limit the input to a reasonable human age range.
if age not in range(0, 126):
    print("Please enter a valid age 0-125.")
elif age <= 2:
    print("You are an infant")
elif age <= 12:
    print("You are a child")
elif age <= 19:
    print("You are a teenager")
elif age <= 64:
    print("You are an adult")
else:
    print("You are a senior")
