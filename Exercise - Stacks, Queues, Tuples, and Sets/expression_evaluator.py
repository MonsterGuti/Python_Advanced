from collections import deque

expressions = input().split()
numbers = deque()

operators = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y
}

for char in expressions:
    if char not in "*+-/":
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            numbers.appendleft(operators[char](first_number, second_number))

print(*numbers)
