import numpy as np

with open("day6text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

equations = np.array([line.split() for line in lines[:4]]).T
symbols = lines[-1].split()

bigtotal = 0
for idx, nums in enumerate(equations):
    op = symbols[idx]
    if op == "*":
        total = 1
        for n in nums:
            total *= int(n)
    else:
        total = 0
        for n in nums:
            total += int(n)

    bigtotal += total
print(bigtotal)
