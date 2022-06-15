def average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        raise ValueError("undefined for empty collection")
