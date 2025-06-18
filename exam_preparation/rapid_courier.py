from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])

total_delivered_weight = 0

while packages and couriers:
    package = packages[-1]
    courier = couriers[0]

    if courier > package:
        if courier - 2 * package > 0:
            couriers[0] -= 2 * package
            couriers.rotate(-1)
        else:
            couriers.popleft()
        packages.pop()
        total_delivered_weight += package

    elif courier == package:
        packages.pop()
        couriers.popleft()
        total_delivered_weight += package

    else:
        packages[-1] -= courier
        couriers.popleft()
        total_delivered_weight += courier

print(f"Total weight: {total_delivered_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")

elif not packages and couriers:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")
