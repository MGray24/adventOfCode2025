with open("day2text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed
import re
line = lines[0]
total = 0
for r in line.split(","):
    s1, s2 = r.split("-")
    i1, i2 = int(s1), int(s2)
    for i in range(i1, i2+1):
        if re.match(r"(\d+)\1$", str(i)):
            total += i

print(total)
