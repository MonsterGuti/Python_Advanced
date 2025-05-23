from collections import deque

petrol_pumps = int(input())
petrol_data = deque()

for _ in range(petrol_pumps):
    amount, dist = input().split()
    petrol_data.append({"fuel": int(amount), "distance": int(dist)})

stops = 0
start_positions = 0
while stops < petrol_pumps:
    fuel = 0
    for i in range(petrol_pumps):
        fuel += petrol_data[i]["fuel"]
        dist = petrol_data[i]["distance"]
        if fuel < dist:
            petrol_data.rotate(-1)
            start_positions += 1
            stops = 0
            break
        fuel -= dist
        stops += 1

print(start_positions)