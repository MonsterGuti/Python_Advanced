from functools import reduce

mapper = {
    "+": lambda *args: reduce(lambda x, y: x + y, args),
    "-": lambda *args: reduce(lambda x, y: x - y, args),
    "*": lambda *args: reduce(lambda x, y: x * y, args),
    "/": lambda *args: reduce(lambda x, y: x / y, args)
}


def operate(operator, *args):
    return mapper[operator](*args)


print(operate("+", 1, 2, 3))
