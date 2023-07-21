#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        print("{:d}{:1d}".format(num1, num2), end=", " if (num1, num2) != (9, 8) else "\n")
