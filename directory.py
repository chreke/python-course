from collections import namedtuple

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def find_employee_by_email(self, email):
        return next(
            (e for e in self.employees if e.email == email),
            None
        )

    def list_employees(self):
        return self.employees


class Employee:
    def __init__(self, name, email, role, salary):
        self.name = name
        self.email = email
        self.role = role
        self.salary = salary

    def __str__(self):
        return f"{name} <{email}>"

    # NB: It could be a good idea to add an __eq__ method here
