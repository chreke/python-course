def parse_csv(iterable):
    headers = next(iterable).strip().split(",")
    for line in iterable:
        row = line.strip().split(",")
        yield dict(zip(headers, row))
