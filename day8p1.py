import math
import itertools
from scipy.cluster.hierarchy import DisjointSet

with open("day8text.txt", "r") as file:
    content = file.read()  # Read file into a string
    lines = content.splitlines() #list with newlines removed

points = [tuple([int(n) for n in line.split(",")]) for line in lines]

dist_list = [(math.dist(points[i], points[j]), i, j) for i, j in itertools.combinations(range(len(points)),2)]

dist_list.sort(key=lambda x:x[0]) # sort by distances

disjoint_set = DisjointSet(points)

con = 0
for dist, i, j in dist_list:

    disjoint_set.merge(points[i], points[j])
    con += 1
    if con == 1000:
        break

biggest_circuits = sorted([len(sub) for sub in disjoint_set.subsets()], reverse=True)

print(biggest_circuits[0]*biggest_circuits[1]*biggest_circuits[2])