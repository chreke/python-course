# Answers to Project Euler exercises

```python
sum(number for number in range(1000) if not (number % 3 and number % 5))
```

```python
# Given that we've defined a fibonacci generator in fibonacci.py
from itertools import takewhile
from fibonacci import fibonacci

sum(x for x in takewhile(lambda x: x <= 1000000, fib()) if x % 2 == 0)
```

# Answers to Employee exercise

```python
from csv import DictReader

with open("employees.csv") as f:
   rows = list(DictReader(f))

max(int(x["Salary"]) for x in rows if x["Role"] == "Software engineer")
# 65000

max_salary = max(int(x["Salary"]) for x in rows)
next(x for x in rows if int(x["Salary"]) == max_salary)
# Max

sum(int(x["Salary"]) for x in rows) / len(rows)
# 53437.5

{x["Role"] for x in rows}
# {'CEO',
#  'Copywriter',
#  'Graphic designer',
#  'HR',
#  'Intern',
#  'Manager',
#  'Sales manager',
#  'Software engineer',
#  'Tech lead'}
```
