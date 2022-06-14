# Answers to Project Euler exercises:

```python
sum(number for number in range(1000) if not (number % 3 and number % 5))
```

```python
# Given that we've defined a fibonacci generator in fibonacci.py
from itertools import takewhile
from fibonacci import fibonacci

sum(x for x in takewhile(lambda x: x <= 1000000, fib()) if x % 2 == 0)
```
