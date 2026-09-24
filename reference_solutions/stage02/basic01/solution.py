grid_rows = ["..#..", ".##..", "?.#.#", "?????", "#..X."]

obstacle_count = 0
unmapped_count = 0
invalid_char_count = 0
first_obstacle_row = -1
first_obstacle_col = -1
rows_skipped = 0

for row_index in range(len(grid_rows)):
    row = grid_rows[row_index]
    if row == "?????":
        rows_skipped += 1
        continue
    for col_index in range(len(row)):
        char = row[col_index]
        if char == "#":
            obstacle_count += 1
            if first_obstacle_row == -1:
                first_obstacle_row = row_index
                first_obstacle_col = col_index
        elif char == "?":
            pass
        elif char == ".":
            pass
        else:
            invalid_char_count += 1
        if char == "?":
            unmapped_count += 1

last_obstacle_row = -1
row_cursor = len(grid_rows) - 1
while row_cursor >= 0:
    if "#" in grid_rows[row_cursor]:
        last_obstacle_row = row_cursor
        break
    row_cursor -= 1
