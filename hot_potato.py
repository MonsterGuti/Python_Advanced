from collections import deque

queue = deque(input().split())
n = int(input())

while len(queue) != 1:
    queue.rotate(-(n - 1))
    print(f"Removed {queue.popleft()}")

print(f"Last is {queue.pop()}")
