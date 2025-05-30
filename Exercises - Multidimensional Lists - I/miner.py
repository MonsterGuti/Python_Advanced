size_of_matrix = int(input())
commands_line = input().split()
matrix = [[col for col in input().split()] for _ in range(size_of_matrix)]

miner_position = (0, 0)
total_coal = 0

for row in range(size_of_matrix):
    for col in range(size_of_matrix):
        if matrix[row][col] == "s":
            miner_position = (row, col)
        elif matrix[row][col] == "c":
            total_coal += 1

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

coal_collected = 0
for command in commands_line:
    new_row = miner_position[0] + directions[command][0]
    new_col = miner_position[1] + directions[command][1]

    if not (0 <= new_row < size_of_matrix and 0 <= new_col < size_of_matrix):
        continue
    miner_position = (new_row, new_col)
    cell = matrix[new_row][new_col]

    if cell == "c":
        coal_collected += 1
        matrix[new_row][new_col] = "*"
        if coal_collected == total_coal:
            print(f"You collected all coal! ({new_row}, {new_col})")
            exit()
    elif cell == "e":
        print(f"Game over! ({new_row}, {new_col})")
        exit()

else:
    print(f"{total_coal - coal_collected} pieces of coal left. ({new_row}, {new_col})")