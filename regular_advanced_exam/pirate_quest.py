size = int(input())
pirate_position = [0, 0]
matrix = []

total_treasures = 0
for row in range(size):
    row_data = list(input())
    for col in range(size):
        if row_data[col] == "S":
            pirate_position = [row, col]
            row_data[col] = "."
        elif row_data[col] == "*":
            total_treasures += 1
    matrix.append(row_data)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

ship_durability = 100
CHARM_POINTS = 25
charm_used = False

while True:
    command = input()
    if command == "stop":
        break

    delta_row, delta_col = directions[command]
    new_row = (pirate_position[0] + delta_row) % size
    new_col = (pirate_position[1] + delta_col) % size
    pirate_position = [new_row, new_col]
    cell = matrix[new_row][new_col]

    if cell == "*":
        total_treasures -= 1
        matrix[new_row][new_col] = "."
    elif cell == "C":
        if not charm_used:
            ship_durability = min(100, ship_durability + CHARM_POINTS)
            charm_used = True
        matrix[new_row][new_col] = "."
    elif cell == "M":
        ship_durability -= CHARM_POINTS
        matrix[new_row][new_col] = "."
        if ship_durability <= 0:
            break

    if total_treasures == 0:
        break

matrix[pirate_position[0]][pirate_position[1]] = "S"

if ship_durability <= 0:
    print(f"Shipwreck! Last known coordinates ({pirate_position[0]}, {pirate_position[1]})")
elif total_treasures == 0:
    print("Yo-ho-ho! All treasure chests collected!")
else:
    print("Retreat! Some treasures remain unclaimed.")

print(f"Ship Durability: {ship_durability}")
if total_treasures > 0:
    print(f"Unclaimed chests: {total_treasures}")

for row in matrix:
    print("".join(row))
