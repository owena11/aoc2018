import sys
from collections import defaultdict

input_list = [ line.strip() for line in open(sys.argv[1])]


triple_count = 0
double_count = 0


def char_count(input_):
    count = defaultdict(int)
    for char in input_:
        count[char] += 1
    return count


for box in input_list:
    count = char_count(box)
    if 2 in count.values():
        double_count += 1
    if 3 in count.values():
        triple_count += 1

checksum = triple_count * double_count

print('Double Count: {},\t Triple Count: {}'.format(double_count, triple_count))
print('checksum: {}'.format(checksum))
