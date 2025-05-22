from collections import deque

food_quantity = int(input())
orders_queue = deque(int(x) for x in input().split())

print(max(orders_queue))

is_enough = True
while orders_queue:
    if orders_queue[0] <= food_quantity:
        food_quantity -= orders_queue[0]
        orders_queue.popleft()
    else:
        is_enough = False
        break

if is_enough:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders_queue))}")
