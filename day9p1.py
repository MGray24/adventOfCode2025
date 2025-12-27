import math
import itertools

with open("day9text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

def area(point1, point2):
    return (abs(point1[0]-point2[0])+1)*(abs(point1[1]-point2[1])+1)

points = [tuple([int(n) for n in line.split(",")]) for line in lines]

area_list = [(area(points[i], points[j]), i, j) for i, j in itertools.combinations(range(len(points)),2)]

max_area = max(area_list, key=lambda x: x[0])

print(max_area[0])