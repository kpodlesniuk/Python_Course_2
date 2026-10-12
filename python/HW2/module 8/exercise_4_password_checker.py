#!/usr/bin/env python3

"""
Exercise 4: Password Checker

Simulate a simple password checker.

- Ask the user to enter a password.
- Continue prompting while the entered password is incorrect.
- Once the correct password is entered, display a success message.
"""

correct_password = "ppp"
entered_password = input("Please enter password: ")

while entered_password != correct_password:
    print("This is not the correct password. Try again.")
    entered_password = input("Please enter password: ")

print("Yoo-Hoo, your password is correct!")
