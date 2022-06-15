import pytest

from directory import Department, Employee

@pytest.fixture
def employees():
    return [
        Employee("Sarah", "sarah@acme.com", "Developer", 50000),
        Employee("Richard", "richard@acme.com", "Copywriter", 40000),
        Employee("Alice", "alice@acme.com", "CTO", 70000)
    ]

@pytest.fixture
def employee(employees):
    return employees[0]


def test_adding_an_employee(employee):
    d = Department("Sales")
    d.add_employee(employee)
    assert employee in d.list_employees()

def test_listing_employees(employees):
    d = Department("Marketing")
    for e in employees:
        d.add_employee(e)
    assert len(d.list_employees()) == len(employees)

def test_finding_employee_by_email(employee):
    d = Department("Sales")
    d.add_employee(employee)
    assert d.find_employee_by_email(employee.email)
