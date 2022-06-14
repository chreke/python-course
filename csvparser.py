def parse_csv(filename):
    rows = []
    with open(filename, "r") as f:
        headers = next(f).strip().split(",")
        for line in f:
            row = line.strip().split(",")
            rows.append(
                dict(zip(headers, row))
            )
    return rows
