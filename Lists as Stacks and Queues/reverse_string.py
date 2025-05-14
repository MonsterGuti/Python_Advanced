user_input = list(input())
stack = []

while user_input:
    stack.append(user_input.pop())

print("".join(stack))