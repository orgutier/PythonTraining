events = ["IN:2", "IN:1", "OUT:1", "SKIP", "BAD", "IN:5", "OUT:2", "IN:0", "OUT:10"]
capacity = 6
sections = 3
rows_per_section = 2
seats_per_row = 2

passengers = 0
trip_ended_early = False
i = 0
while i < len(events):
    event = events[i]
    if event.startswith("IN:"):
        n = int(event.split(":")[1])
        if passengers + n > capacity:
            trip_ended_early = True
            break
        passengers += n
    elif event.startswith("OUT:"):
        n = int(event.split(":")[1])
        passengers -= n
        if passengers < 0:
            passengers = 0
    elif event == "SKIP":
        i += 1
        continue
    else:
        pass
    i += 1

total_seats = 0
for section in range(sections):
    for row in range(rows_per_section):
        total_seats += seats_per_row

capacity_is_valid = capacity <= total_seats
