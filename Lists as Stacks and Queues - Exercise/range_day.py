n = 5
matrix = []
my_position = [0, 0]
targets = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets +=  1

possible_moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1)
}
targets_down = []

for _ in range(int(input())):
    command = input().split()

    if command[0] == "shoot":
        r = my_position[0] + possible_moves[command[1]][0]
        c = my_position[1] + possible_moves[command[1]][1]
        while 0 <= r < n and 0 <= c < n:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                targets -= 1
                targets_down.append([r, c])
                break
            r += possible_moves[command[1]][0]
            c += possible_moves[command[1]][1]

        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break
    elif command[0] == "move":
        r = my_position[0] + possible_moves[command[1]][0] * int(command[2])
        c = my_position[1] + possible_moves[command[1]][1] * int(command[2])
        if 0 <= r < n and 0 <= c < n and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[my_position[0]][my_position[1]] = "."
            my_position = [r, c]


if targets:
    print(f"Training not completed! {targets} targets left.")
[print(row) for row in targets_down]
