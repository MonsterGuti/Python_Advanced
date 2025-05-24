from collections import deque

cups_capacity = deque(int(x) for x in input().split())
bottles_count = [int(x) for x in input().split()]
wasted_liters = 0

while cups_capacity and bottles_count:
    if bottles_count[-1] >= cups_capacity[0]:
        wasted_liters += bottles_count.pop() - cups_capacity.popleft()
    else:
        cups_capacity[0] -= bottles_count.pop()

if not cups_capacity:
    print(f"Bottles: {' '.join(map(str, bottles_count))}")

elif not bottles_count:
    print(f"Cups: {' '.join(map(str, cups_capacity))}")

print(f"Wasted litters of water: {wasted_liters}")
