#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-100, 100)

# Check whether the number is positive, negative, or zero and print the corresponding message
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
elif number < 0:
    print(f"{number} is negative")
