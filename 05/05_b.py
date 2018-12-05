import sys
import string
from collections import deque

input_string = open(sys.argv[1]).readline().strip()


def react_polymer(input_string):
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
    return accepted


output_dict = {}

for char in string.ascii_lowercase:
    removed_lower_str = input_string.replace(char, '')
    removed_str = removed_lower_str.replace(char.upper(), '')
    output_dict[char] = len(react_polymer(removed_str))

print('Output_dict: {}'.format(output_dict))
print('Accepted polymer length: {}'.format(min(output_dict.values())))
