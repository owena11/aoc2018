import sys
import re
import math
from collections import defaultdict

input_list = [ line.strip() for line in open(sys.argv[1])]

#1 @ 527,351: 24x10
# Group 1 - ID, Group 2 - X, Group 3 - Y, Group 4 patch width,
# Group 5 - patch height
extract_sizes =  re.compile("#(\d+)\s*@\s*(\d+),(\d+):\s*(\d+)x(\d+)")
result = extract_sizes.match(input_list[0])

cut_dict = {}
for cut in input_list:
    result = extract_sizes.match(cut)
    cut_dict[result.group(1)] = [[ int(result.group(2)), int(result.group(3))],
                                 [ int(result.group(4)), int(result.group(5))]]

loc_count = defaultdict(int)


for cut in  cut_dict.values():
    start_x, end_x = cut[0][0], cut[1][0] + cut[0][0]
    start_y, end_y = cut[0][1], cut[1][1] + cut[0][1]
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            loc_count[(x,y)] += 1


for id_, cut in cut_dict.items():
    start_x, end_x = cut[0][0], cut[1][0] + cut[0][0]
    start_y, end_y = cut[0][1], cut[1][1] + cut[0][1]

    cut_overlaps = []
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            cut_overlaps += [loc_count[(x,y)]]

    if all( overlap == 1 for overlap in cut_overlaps):
        valid_id = id_
        break

print('Id of non overlapping square: {}'.format(valid_id))

