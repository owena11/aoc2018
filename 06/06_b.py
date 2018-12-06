from collections import defaultdict
import math
import re
import sys

input_list=  [ list(map(int,re.findall(r'-?\d+', line))) for line in open(sys.argv[1])]

# Find the maximum and min coordinate in x and y
x_max = max(input_list, key = lambda x:  x[0])[0]
x_min = min(input_list, key = lambda x:  x[0])[0]

y_max = max(input_list, key = lambda x:  x[1])[1]
y_min = min(input_list, key = lambda x:  x[1])[1]


def manhatan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# For every point within our bounded space, work out the closest  point via
# manhatan distance.

distance_count = defaultdict(int)
inf_areas = [False]*len(input_list)


point_count = 0

for x in range(x_min, x_max+1):
    for y in range(y_min, y_max+1):
        bounded_coord = [x,y]

        distances = [ None] * len(input_list)

        for i, point in enumerate(input_list):
            distances[i] = manhatan(bounded_coord, point)

        sum_dist =  sum(distances)

        if sum_dist < 10000:
            point_count += 1

# No we just find the min of the dictionary that isnt a boundary point

print('Areas with distances < 10000: {}'.format(point_count))
