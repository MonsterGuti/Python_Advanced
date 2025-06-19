def changed_position(position_of_player, new_direction):
    return [
        position_of_player[0] + new_direction[0],
        position_of_player[1] + new_direction[1]
    ]

size = int(input())
player_position = [0, 0]
matrix = []

for row in range(size):
    row_data = input().split()
    matrix.append(row_data)
    for col in range(size):
        if matrix[row][col] == "P":
            player_position = [row, col]

STARS_GOAL = 10
collected_stars = 2

mapper_position = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

first_move = True

while 0 < collected_stars < STARS_GOAL:
    command = input().strip()
    if command not in mapper_position:
        continue

    next_position = changed_position(player_position, mapper_position[command])

    if first_move:
        matrix[player_position[0]][player_position[1]] = "."
        first_move = False

    if not (0 <= next_position[0] < size and 0 <= next_position[1] < size):
        matrix[player_position[0]][player_position[1]] = "."
        player_position = [0, 0]
        if matrix[0][0] == "*":
            collected_stars += 1
            matrix[0][0] = "."
        matrix[0][0] = "P"
        continue

    cell = matrix[next_position[0]][next_position[1]]

    if cell == "*":
        collected_stars += 1
        matrix[player_position[0]][player_position[1]] = "."
        matrix[next_position[0]][next_position[1]] = "P"
        player_position = next_position
        if collected_stars == STARS_GOAL:
            break

    elif cell == "#":
        collected_stars -= 1
        if collected_stars <= 0:
            break
        matrix[player_position[0]][player_position[1]] = "P"
        continue

    else:
        matrix[player_position[0]][player_position[1]] = "."
        matrix[next_position[0]][next_position[1]] = "P"
        player_position = next_position

if matrix[player_position[0]][player_position[1]] != "P":
    matrix[player_position[0]][player_position[1]] = "P"

if collected_stars == STARS_GOAL:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{player_position[0]}, {player_position[1]}]")
[print(' '.join(row)) for row in matrix]
