"""
OOP I -- Employee Registry
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage06_exercise02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage06/exercise02/ and import it as a submodule (e.g.
`from exercises.stage06.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Employee:
    company_name = "Acme Corp"
    employee_count = 0

    def __init__(self, name: str, salary: float):
        raise NotImplementedError

    @classmethod
    def get_employee_count(cls) -> int:
        """cls.employee_count."""
        raise NotImplementedError

    @classmethod
    def hire_intern(cls, name: str) -> "Employee":
        """cls(name, salary=0) -- an alternate constructor."""
        raise NotImplementedError

    @staticmethod
    def is_valid_salary(salary) -> bool:
        """salary >= 0."""
        raise NotImplementedError
