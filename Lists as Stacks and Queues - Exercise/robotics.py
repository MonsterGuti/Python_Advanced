from collections import deque
from datetime import datetime, timedelta

robot_info = input().split(";")
robots = []

for robot in robot_info:
    name, time = robot.split("-")
    robots.append({
        "name": name,
        "time": time,
        "available_at": 0
    })

start_time_str = input()
start_time = datetime.strptime(start_time_str, "%H:%M:%S")
current_time = start_time

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

time_in_seconds = 0

while products:
    time_in_seconds += 1
    current_time = start_time + timedelta(seconds=time_in_seconds)
    product = products.popleft()
    assigned = False

    for robot in robots:
        if time_in_seconds >= robot["available_at"]:
            robot["available_at"] = time_in_seconds + int(robot["time"])
            print(f'{robot["name"]} - {product} [{current_time.strftime("%H:%M:%S")}]')
            assigned = True
            break
    if not assigned:
        products.append(product)
