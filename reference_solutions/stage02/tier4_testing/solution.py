numbers = [4, 7, 2, 9, 3, 5, 8]
threshold = 5

target_count_v1 = 0
for n in numbers:
    if n > threshold:
        target_count_v1 += 1

target_count_v2 = 0
for n in numbers:
    if n >= threshold:
        target_count_v2 += 1

target_first_over_v1 = None
for n in numbers:
    if n > threshold:
        target_first_over_v1 = n
        break

target_first_over_v2 = None
for n in numbers:
    if n > threshold:
        target_first_over_v2 = n

check_results = []

expected_count = sum(1 for n in numbers if n > threshold)
check_results.append(("target_count_v1 meets spec", target_count_v1 == expected_count))
check_results.append(("target_count_v2 meets spec", target_count_v2 == expected_count))

expected_first_over = next((n for n in numbers if n > threshold), None)
check_results.append(("target_first_over_v1 meets spec", target_first_over_v1 == expected_first_over))
check_results.append(("target_first_over_v2 meets spec", target_first_over_v2 == expected_first_over))

total_checks = len(check_results)
passed_checks = sum(1 for _, ok in check_results if ok)
failed_descriptions = [desc for desc, ok in check_results if not ok]
