def fibonacci():
    yield 1
    current = 2
    previous = 1
    while True:
        yield current
        current, previous = previous + current, current
