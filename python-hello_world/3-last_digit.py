#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10
last_digit_with_sign = -last_digit if number < 0 else last_digit

# Print the message with the number and its last digit using f-string
print(f"Last digit of {number} is {last_digit_with_sign} and is", end=" ")

# Check whether the last digit is greater than 5, 0, or less than 6 but not 0 and print the corresponding message
if last_digit_with_sign > 5:
    print("greater than 5")
elif last_digit_with_sign == 0:
    print("0")
elif last_digit_with_sign < 6:
    print("less than 6 and not 0")
