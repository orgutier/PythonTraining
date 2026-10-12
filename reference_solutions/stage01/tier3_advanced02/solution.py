base_text = "97"
exponent_text = "42"

base = int(base_text)
exponent = int(exponent_text)

huge_power = base ** exponent
huge_power_digit_count = len(str(huge_power))

small_int_a = 100
small_int_b = 100
small_ints_share_identity = small_int_a is small_int_b

large_int_from_literal = 1_000_000
large_int_from_conversion = int("1000000")
large_ints_share_identity = large_int_from_literal is large_int_from_conversion

string_literal_a = "python_stage01"
string_literal_b = "python_stage01"
string_literals_share_identity = string_literal_a is string_literal_b

string_built_at_runtime = "".join(["python_", "stage01"])
runtime_string_shares_identity = string_literal_a is string_built_at_runtime

print(f"huge_power has {huge_power_digit_count} digits")
