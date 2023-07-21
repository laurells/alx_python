pairs = []
for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        pairs.append("{:d}{:1d}".format(num1, num2))

print(", ".join(pairs))
