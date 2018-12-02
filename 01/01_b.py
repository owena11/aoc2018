from itertools import cycle, islice
from collections import defaultdict
import sys

input_list =  [int(line.strip()) for line in open(sys.argv[1])]
input_list_len = len(input_list)
# Set up a endless cycle of the freq changes
freq_cycle = cycle(input_list)

observed_freqs = defaultdict(lambda  : False)
current_freq = 0

for i, freq_change in enumerate(freq_cycle):
    if i % input_list_len == 0:
        print('Iterated input list {} times'.format( i // input_list_len))
        print('Current freq {}'.format(current_freq))

    current_freq += freq_change
    if observed_freqs[current_freq]:
        break
    observed_freqs[current_freq] = True



print('Calibrated frequency: {}'.format(current_freq))
