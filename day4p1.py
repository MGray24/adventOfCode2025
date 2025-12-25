with open("day4text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

rolls_accessed = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        adjacent = 0
        if lines[y][x] == "@":
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i != 0 or j != 0) and y+i>=0 and x+j>=0:
                        try:
                            sym = lines[y+i][x+j]
                            if sym == "@":
                                adjacent += 1
                        except:
                            pass
            if adjacent < 4:
                rolls_accessed += 1

print(rolls_accessed)
