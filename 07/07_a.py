import sys
from collections import defaultdict, OrderedDict

input_constraints = [ (line[5], line[36]) for line in open(sys.argv[1])]

# Find out all fo the constriants
instruction_constraints = defaultdict(list)
for instruction in input_constraints:
    # Touch both instructions to there is a record of them existing
    instruction_constraints[instruction[0]]
    instruction_constraints[instruction[1]] += [instruction[0]]

sorted_constraints = OrderedDict(sorted(instruction_constraints.items()))


instruction_order = []

while len(sorted_constraints.keys()) != 0:
    for key, values in sorted_constraints.items():
        # Item found with no constraints
        if len(values) == 0:
            instruction_order += [key]
            # Remove the instruction form the dict now we are done with it.
            sorted_constraints.pop(key)
            # remove the key as a constraint from instructions
            for constraints in  sorted_constraints.values():
                try:
                    constraints.pop(constraints.index(key))
                except ValueError as e:
                    pass

            # Restart the seatch for a constraint free item

            break


print('Instruction order: {}'.format(''.join(instruction_order)))
