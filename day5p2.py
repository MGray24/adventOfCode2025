import numpy as np

with open("day5text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

middle = lines.index("")
ranges = [i.split("-") for i in lines[:middle]]
ids = lines[middle+1:]

ranges.sort(key=lambda x:int(x[0]))

freshids = 0
prevend = 0
for range in ranges:
    start = int(range[0])
    if start > prevend:
        prevend = int(range[1])
        freshids += prevend - start + 1
    elif int(range[1]) <= prevend:
        continue
    else:
        freshids += int(range[1]) - prevend
        prevend = int(range[1])

print(freshids)


