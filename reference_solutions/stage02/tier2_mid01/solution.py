scheduled_names = ["Ana", "Ben", "Cy", "Dee", "Ella"]
checked_in_names = ["Ben", "Dee", "Ana"]
shift_hours = [8, 6, 10, 4, 9]
max_hours = 9

for name in scheduled_names:
    if name not in checked_in_names:
        all_checked_in = False
        break
else:
    all_checked_in = True

missing_list = []
for name in scheduled_names:
    if name not in checked_in_names:
        missing_list.append(name)

first_missing_has_long_shift = (
    len(missing_list) > 0
    and shift_hours[scheduled_names.index(missing_list[0])] > max_hours
)

coverage_status = "full" if len(missing_list) == 0 else "short-staffed"

overtime_names = []
for name, hours in zip(scheduled_names, shift_hours):
    if hours > max_hours:
        overtime_names.append(name)
