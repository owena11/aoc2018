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

for x in range(x_min, x_max+1):
    for y in range(y_min, y_max+1):
        bounded_coord = [x,y]

        distances = [ None] * len(input_list)

        for i, point in enumerate(input_list):
            distances[i] = manhatan(bounded_coord, point)

        min_dist =  min(distances)
        min_points = [ i for i, dist in enumerate(distances) if dist == min_dist]


        if len(min_points) == 1:
            distance_count[min_points[0]] += 1
            if bounded_coord[0] in [x_max, x_min] or bounded_coord[1] in [y_max, y_min]:
                inf_areas[min_points[0]] = True
            # If the point exists on the boundarty it will expand to infiinitie
            # area, flag point here.

# No we just find the min of the dictionary that isnt a boundary point
for point, area in sorted(distance_count.items(), key =lambda x: -1*x[1]):
    if not inf_areas[point]:
        break
    #pass

print('Largest bounded area: {} from point {}'.format(area, point))
