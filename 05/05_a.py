import sys
from collections import deque

input_string = open(sys.argv[1]).readline().strip()
accepted = []

for char in input_string:
    # Special case where the list is empty
    if len(accepted) == 0:
        accepted.append(char)
        continue
    # Otherwise preform the comparison
    tail_char = accepted[len(accepted)-1]
    if abs(ord(tail_char) - ord(char)) == 32:
        accepted.pop()
    else:
        accepted.append(char)

print('Accepted polymer length: {}'.format(len(accepted)))
