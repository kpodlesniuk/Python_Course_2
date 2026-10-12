#!/usr/bin/env python3

"""
Exercise 5: Prime Number Checker

Check whether a given positive integer is a prime number.

- Ask the user to enter a positive integer.
- Use a while loop to determine whether the number is prime.
- Display the result.
"""

number = int(input("Please enter a positive integer: "))

if number <= 0:
    print("The number is not positive, please try again")
elif number == 1:
    print("One is not a prime number")
else:
    divisor = 2
    prime = True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break

        divisor += 1

    if prime:
        print("The number is a prime number")
    else:
        print("The number is not prime, there is a divisor:", divisor)
