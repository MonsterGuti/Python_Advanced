stack = []
n = int(input())

commands = {
    "1": lambda x: stack.append(int(x)),
    "2": lambda: stack.pop() if stack else None,
    "3": lambda: print(max(stack)) if stack else None,
    "4": lambda: print(min(stack)) if stack else None,
}

for _ in range(n):
    query = input().split()
    commands[query[0]](*query[1:])

if stack:
    print(", ".join(map(str, reversed(stack))))