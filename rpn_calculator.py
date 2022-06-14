import operator

def calculate(expression):
    operators = {
        "+": operator.add,
        "/": operator.truediv,
        "*": operator.mul,
        "-": operator.sub,
    }
    stack = []
    for token in expression.split():
        if op := operators.get(token):
            stack.append(op(stack.pop(), stack.pop()))
        else:
            stack.append(float(token))
    return stack[0]
