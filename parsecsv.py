def parse_csv(lines):
    lines = iter(lines)
    headers = next(lines).strip().split(",")
    for line in lines:
        row = line.strip().split(",")
        yield dict(zip(headers, row))
