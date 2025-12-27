import math
import itertools
from shapely import Polygon, box


with open("day9text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

def area(point1, point2):
    return (abs(point1[0]-point2[0])+1)*(abs(point1[1]-point2[1])+1)

points = [tuple([int(n) for n in line.split(",")]) for line in lines]

# Build polygon from red points (loop order!)
poly = Polygon(points)

best = 0
best_pair = None

for i, j in itertools.combinations(range(len(points)), 2):
    p1 = points[i]
    p2 = points[j]

    # Skip degenerate rectangles
    if p1[0] == p2[0] or p1[1] == p2[1]:
        continue

    rect = box(
        min(p1[0], p2[0]),
        min(p1[1], p2[1]),
        max(p1[0], p2[0]),
        max(p1[1], p2[1])
    )

    if poly.contains(rect):
        a = area(p1, p2)
        if a > best:
            best = a
            best_pair = (p1, p2)

print(best)
print(best_pair)