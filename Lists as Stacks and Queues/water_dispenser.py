from collections import deque

liters = int(input())
queue = deque()

while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

while True:
    command = input()
    if command == "End":
        break
    elif command.startswith("refill"):
        _, refill_liters = command.split()
        liters += int(refill_liters)
    else:
        requested = int(command)
        if requested <= liters:
            print(f"{queue.popleft()} got water")
            liters -= requested
        else:
            print(f"{queue.popleft()} must wait")

print(f"{liters} liters left")
