# a program that prints numbers from 0 to 99
#!/usr/bin/python3
for num in range(100):
    print(f"{num:02d}", end=(", " if num < 99 else "\n"))
