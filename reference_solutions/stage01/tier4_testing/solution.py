price_text = "19.99"
quantity_text = "3"
discount_flag_text = "False"

target_total_v1 = float(price_text) * int(quantity_text)
target_total_v2 = float(price_text) + int(quantity_text)

target_is_discounted_v1 = discount_flag_text == "True"
target_is_discounted_v2 = bool(discount_flag_text)

check_results = []

expected_total = float(price_text) * int(quantity_text)
check_results.append(("target_total_v1 meets spec", target_total_v1 == expected_total))
check_results.append(("target_total_v2 meets spec", target_total_v2 == expected_total))

expected_is_discounted = discount_flag_text == "True"
check_results.append(("target_is_discounted_v1 meets spec", target_is_discounted_v1 == expected_is_discounted))
check_results.append(("target_is_discounted_v2 meets spec", target_is_discounted_v2 == expected_is_discounted))

total_checks = len(check_results)
passed_checks = sum(1 for _, ok in check_results if ok)
failed_descriptions = [desc for desc, ok in check_results if not ok]
