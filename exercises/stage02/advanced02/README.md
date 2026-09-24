# Round-Robin Task Scheduler

Given, don't modify:

```python
workers = ["alpha", "beta", "gamma"]
morning_tasks = ["t1", "t2", "t3"]
afternoon_tasks = ["t4", "t5", "t6", "t7"]
```

Using `itertools`, write plain top-level code that computes:

- `all_tasks` -- `morning_tasks` followed by `afternoon_tasks`, via `list(itertools.chain(morning_tasks, afternoon_tasks))` (not `morning_tasks + afternoon_tasks`).
- `assignments` -- each task in `all_tasks` paired round-robin with a worker, via `list(zip(all_tasks, itertools.cycle(workers)))`. Because `itertools.cycle` repeats `workers` forever and `zip` stops at the shorter of its two inputs, this naturally stops once `all_tasks` runs out, cycling back through `workers` as many times as needed.
- `first_three_assignments` -- just the first 3 pairs of `assignments`, via `list(itertools.islice(assignments, 3))` (not `assignments[:3]`).
- `worker_task_counts` -- a `dict` mapping each worker to how many tasks they were assigned, built with a plain `for task, worker in assignments:` loop and `worker_task_counts[worker] = worker_task_counts.get(worker, 0) + 1`.
