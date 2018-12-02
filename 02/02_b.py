import sys
from collections import defaultdict
from itertools import combinations

input_list = [line.strip() for line in open(sys.argv[1])]

def str_diff(a, b):
    diff = 0
    diff_locs = []
    for i, chars in enumerate(zip(a,b)):
        if chars[0] != chars[1]:
            diff += 1
            diff_locs += [i]

    return diff, diff_locs

for box_a, box_b in combinations(input_list, 2):
    diff, diff_locs = str_diff(box_a, box_b)
    if diff == 1:
        box_id = box_a.replace(box_a[diff_locs[0]], "")

print('Common letters: {}'.format(box_id))
