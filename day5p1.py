import numpy as np

with open("day5text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

middle = lines.index("")
ranges = [i.split("-") for i in lines[:middle]]
ids = lines[middle+1:]

freshids = 0
for id in ids:
    intid = int(id)
    for range in ranges:
        if intid >= int(range[0]) and intid <= int(range[1]):
            freshids += 1
            break
print(freshids)
