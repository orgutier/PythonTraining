import itertools

workers = ["alpha", "beta", "gamma"]
morning_tasks = ["t1", "t2", "t3"]
afternoon_tasks = ["t4", "t5", "t6", "t7"]

all_tasks = list(itertools.chain(morning_tasks, afternoon_tasks))
assignments = list(zip(all_tasks, itertools.cycle(workers)))
first_three_assignments = list(itertools.islice(assignments, 3))

worker_task_counts = {}
for task, worker in assignments:
    worker_task_counts[worker] = worker_task_counts.get(worker, 0) + 1
