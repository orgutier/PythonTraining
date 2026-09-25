item_names = ["bolts", "screws", "washers", "nuts"]
stock_levels = [12, 0, 5, 3]
reorder_threshold = 4

i = 0
while i < len(stock_levels):
    if stock_levels[i] == 0:
        break
    i += 1
else:
    i = -1
out_of_stock_index = i

needs_urgent_reorder = out_of_stock_index != -1 and item_names[out_of_stock_index] != ""

stock_status = "critical" if out_of_stock_index != -1 else "ok"

low_stock_items = []
for name, level in zip(item_names, stock_levels):
    if level < reorder_threshold:
        low_stock_items.append(name)
