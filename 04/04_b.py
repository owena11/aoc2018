from collections import defaultdict
from datetime import datetime
from itertools import zip_longest
import math
import sys
import re

input_text = [line for line in open(sys.argv[1])]

date_extraction  = re.compile('^\[(.*)\](.*#(\d+).*|.*)')
seperated_str =  [date_extraction.match(line).groups() for line in input_text]
seperated_str =  [ (datetime.strptime(group[0], "%Y-%m-%d %H:%M"), *group[1:]) for group in seperated_str]

# Order the events now they are sepereated
seperated_str  =  sorted(seperated_str, key=lambda x:x[0])

def group_by_shift(iter_):
    """ Iterates the sorted timestamps grouping by shifts.
    """
    shift_list = []
    for item in iter_:
        if item[2] is not None and len(shift_list) > 0:
            yield shift_list
            shift_list = []
        shift_list += [item]

    yield shift_list


# Step through the list accuminating with total mins asleep
guards_sleep_patterns = defaultdict( lambda : defaultdict(int) )
for shift in  group_by_shift(seperated_str):
    guard_id = shift[0][2]
    iter_ = [iter(shift[1:])] * 2
    for  sleep, wake in zip_longest(*iter_ ):
        time_asleep = int((wake[0]-sleep[0]).total_seconds() // 60)
        for i in range(sleep[0].minute , sleep[0].minute + time_asleep):
            guards_sleep_patterns[guard_id][i % 60] += 1

max_time_asleep = -1 * math.inf
for guard in guards_sleep_patterns.items():
    most_sleep = max(guard[1].items(), key=lambda x:x[1])
    if most_sleep[1] > max_time_asleep:
        guard_id = guard[0]
        min_asleep = most_sleep[0]
        max_time_asleep = most_sleep[1]

print('Guard id {}, min alseep {}, ans {}'.format(guard_id, min_asleep, int(guard_id)* min_asleep))
