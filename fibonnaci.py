def fibonacci():
    prev = 1
    current = 2
    yield prev
    while True:
        yield current
        current, prev = prev + current, current

