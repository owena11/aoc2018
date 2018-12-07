import sys
from collections import defaultdict, OrderedDict, deque

input_constraints = [ (line[5], line[36]) for line in open(sys.argv[1])]

instruction_constraints = defaultdict(list)
for instruction in input_constraints:
    # Touch both instructions to there is a record of them existing
    instruction_constraints[instruction[0]]
    instruction_constraints[instruction[1]] += [instruction[0]]

sorted_constraints = OrderedDict(sorted(instruction_constraints.items()))


instruction_order = []

job_time = lambda x : (ord(x) - 64)  + 60
n_workers = 5 
worker_tasks = [None] * n_workers

# job complete
def complete_job(key,  sorted_constraints):
    for constraints in  sorted_constraints.values():
        try:
            constraints.pop(constraints.index(key))
        except ValueError as e:
            pass

def get_next_jobs(sorted_constraints):
    avalible_jobs = []
    for key, values in sorted_constraints.items():
        # Item found with no constraints
        if len(values) == 0:
            # Remove the instruction form the dict now we are done with it.
            # remove the key as a constraint from instructions
            # Restart the seatch for a constraint free item
            avalible_jobs += [[key, job_time(key)]]

    for job in avalible_jobs:
        sorted_constraints.pop(job[0])
    return avalible_jobs

returning_jobs = deque()
time_step = 0
done = []
while len(sorted_constraints.keys()) != 0:
    # For workers that have no job assign them one job to work on.
    free_jobs = get_next_jobs(sorted_constraints)
    returning_jobs.extend(free_jobs)
    # Assign Free
    for i, worker in  enumerate(worker_tasks):
        if worker == None:
            if len(returning_jobs) > 0:
                worker_tasks[i] = returning_jobs.popleft()

    # Execute unit of work
    for i, worker in  enumerate(worker_tasks):
        if not  worker == None:
            worker_tasks[i][1] -= 1
            if worker_tasks[i][1] == 0:
               complete_job(worker_tasks[i][0], sorted_constraints)
               done += [worker_tasks[i][0]]
               worker_tasks[i] = None

    time_step += 1

# Clean up and workers left working
while len(worker_tasks) > 0: 
    for i, worker in  enumerate(worker_tasks):
        if not  worker == None:
            worker_tasks[i][1] -= 1
            if worker_tasks[i][1] == 0:
               complete_job(worker_tasks[i][0], sorted_constraints)
               done += [worker_tasks[i][0]]
               worker_tasks[i] = None
        else:
            worker_tasks.pop(i)

    time_step += 1

# Account for overshoopt
time_step -=1

print('Completed in n timesteps: {}'.format(time_step))
print(time_step, worker_tasks, returning_jobs, done)
