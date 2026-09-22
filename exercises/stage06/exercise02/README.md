# Employee Registry

Implement `Employee`:

- `company_name = "Acme Corp"` and `employee_count = 0` -- **class** attributes, declared directly in the class body (already in the stub). Every instance shares the *same* `company_name` unless overridden on that instance.
- `__init__(self, name: str, salary: float)` -- set the **instance** attributes `self.name` and `self.salary`, then increment the shared class attribute via `Employee.employee_count += 1` (not `self.employee_count`, which would create a new *instance* attribute shadowing the class one instead of incrementing the shared counter).
- `get_employee_count(cls) -> int` (`@classmethod`) -- return `cls.employee_count`.
- `hire_intern(cls, name: str) -> "Employee"` (`@classmethod`) -- return `cls(name, salary=0)`. This is the classic "alternate constructor" use of `@classmethod`: it receives the class itself (`cls`) rather than an instance (`self`), so it can build and return a new instance.
- `is_valid_salary(salary) -> bool` (`@staticmethod`) -- `True` if `salary >= 0`.

See the Study Reference presentation, Topic 6, for the theory.
