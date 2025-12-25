with open("day3text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

total = 0
for line in lines:
    num1 = max([int(i) for i in line[:-1]])
    idx1 = line[:-1].index(str(num1))
    num2 = max([int(i) for i in line[idx1+1:]])
    total += int(f"{num1}{num2}")

print(total)