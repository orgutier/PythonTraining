class Employee:
    company_name = "Acme Corp"
    employee_count = 0

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls) -> int:
        return cls.employee_count

    @classmethod
    def hire_intern(cls, name: str) -> "Employee":
        return cls(name, salary=0)

    @staticmethod
    def is_valid_salary(salary) -> bool:
        return salary >= 0
