def fizzbuzz(integer):
    if integer % 3 == 0 and integer % 5 == 0:
        return "FizzBuzz"
    if integer % 3 == 0:
        return "Fizz"
    if integer % 5 == 0:
        return "Buzz"
    return str(integer)
