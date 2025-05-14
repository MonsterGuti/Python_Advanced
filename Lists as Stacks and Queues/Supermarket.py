from collections import deque
queue = deque()

while True:
    name = input()
    if name == "End":
        break
    if name != "Paid":
        queue.append(name)
    else:
        for i in range(len(queue)):
            print(queue.popleft())


print(f"{len(queue)} people remaining.")