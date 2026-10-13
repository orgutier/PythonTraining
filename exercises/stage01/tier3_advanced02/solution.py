"""
Python Fundamentals -- Big Numbers and String Identity
Write plain top-level code below -- no function/class wrapper needed (or expected) for this one. Assign your answers to the exact variable names named in README.md; the tests import this module and read those variables directly.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage01_tier3_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage01/tier3_advanced02/ and import it as a submodule (e.g.
`from exercises.stage01.tier3_advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


base_text = "97"
exponent_text = "42"


# Write your code here: cast base/exponent, compute huge_power and its
# digit count, then work through the small-int-caching, large-int, and
# string-interning identity checks described in README.md.


base: int = int(base_text)
exponent: int = int(exponent_text)

huge_power: int = base ** exponent
huge_power_digit_count: int = len(str(huge_power))

small_int_a: int = 100
small_int_b: int = 100

small_ints_share_identity: bool = small_int_a is small_int_b

large_int_from_literal: int = 1_000_000
large_int_from_conversion: int = int("1000000")
large_ints_share_identity: bool = large_int_from_literal is large_int_from_conversion

string_literal_a: str="python_stage01"
string_literal_b: str="python_stage01"
string_literals_share_identity: bool = string_literal_a is string_literal_b

string_built_at_runtime: str = "".join(["python", "_stage01"]) # join() es una forma de construir strings a 
#partir de listas de strings y es útil para construir strings a partir de múltiples partes. En este caso, se está construyendo 
#el string "python_stage01" a partir de la lista ["python", "_stage01"]. Es importante notar que hay que poner algo entre las comillas para que no se genere un string vacío, ya que si se pone un string vacío, el resultado sería un string vacío. 
#En este caso, se está poniendo un string vacío entre las comillas para que no se genere un string vacío.
runtime_string_shares_identity: bool = string_literal_a is string_built_at_runtime
print(string_built_at_runtime)

print(f"huge_power_digit_count: {huge_power_digit_count}")

