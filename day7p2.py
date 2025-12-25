import numpy as np

with open("day7text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

current_tachyons = np.zeros(len(lines[0]))
current_tachyons[lines[0].index("S")] = 1

timelines = 1
for line in lines[1:]:
    for idx, char in enumerate(line):
        if idx == 0 or idx == len(line):
            continue
        if current_tachyons[idx] >= 1 and char == '^':
            timelines += current_tachyons[idx]
            current_tachyons[idx-1] += current_tachyons[idx]
            current_tachyons[idx+1] += current_tachyons[idx]
            current_tachyons[idx] = 0
print(timelines)