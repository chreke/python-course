from operator import add, mul, truediv, sub

def evaluate(expression):
    stack = []
    operators = {
        "+": add,
        "*": mul,
        "/": truediv,
        "-": sub
    }
    for token in expression.split():
        if operator := operators.get(token):
            second, first = stack.pop(), stack.pop()
            result = operator(first, second)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]
