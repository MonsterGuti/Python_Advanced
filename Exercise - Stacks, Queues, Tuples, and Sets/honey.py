from collections import deque

bees = deque(int(x) for x in input().split())
nectar_values = [int(x) for x in input().split()]
symbols = deque(input().split())
honey_gain = 0

operators = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y if y != 0 else 0
}

while bees and nectar_values:
    if nectar_values[-1] >= bees[0]:
        honey_gain += abs(operators[symbols.popleft()](bees.popleft(), nectar_values.pop()))
    else:
        nectar_values.pop()

print(f"Total honey made: {honey_gain}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar_values:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_values)}")
