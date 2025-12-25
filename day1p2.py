with open("day1text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

current = 50
total_zeros = 0
for line in lines:
    d = line[0]
    if d == "R":
        for i in range(int(line[1:])):
            current += 1
            if current % 100 == 0:
                total_zeros += 1
    else:
        for i in range(int(line[1:])):
            current -= 1
            if current % 100 == 0:
                total_zeros += 1

print(total_zeros)
