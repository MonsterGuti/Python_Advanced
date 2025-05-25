number_of_commands = int(input())
parking = set()

for _ in range(number_of_commands):
    direction, number = input().split(", ")
    if direction == "IN":
        parking.add(number)
    elif direction == "OUT":
        parking.remove(number)

if not parking:
    print("Parking Lot is Empty")
    exit()

for car_number in parking:
    print(car_number)