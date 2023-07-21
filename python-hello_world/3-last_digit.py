#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10

# Print the message with the number and its last digit using f-string
print(f"Last digit of {number} is {last_digit} and is", end=" ")

# Check whether the last digit is greater than 5, 0, or less than 6 but not 0 and print the corresponding message
if last_digit > 5:
    print("and is greater than 5\n")
elif last_digit == 0:
    print("and is 0\n")
else:
    print("and is less than 6 and not 0\n")
