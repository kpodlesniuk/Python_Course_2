#!/usr/bin/env python3

"""
Exercise 6: Prime Numbers

Find and print all prime numbers between 1 and 50.

- Use a for loop to iterate through the numbers from 1 to 50.
- Determine whether each number is prime.
- Print all prime numbers.
"""

prime_numbers = []

for number in range(2, 51):
    divisor = 2
    prime = True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break

        divisor += 1

    if prime:
        prime_numbers.append(number)

print("The list of prime numbers:", prime_numbers)
