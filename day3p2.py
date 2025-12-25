with open("day3text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

c = 0
n= 12
for i in lines:
    i+=" "
    ind = 0
    l =""
    for p in range(0,n):
        a = max(i[ind:p-n])
        ind += i[ind:p-n].index(a)+1
        l += a
    c+= int(l)
print("\n")
print(c)