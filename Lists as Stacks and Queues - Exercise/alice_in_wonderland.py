n = int(input())

matrix = []
alice_position = [0, 0]

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            alice_position = [row, col]
            matrix[row][col] = "*"

possible_moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

bags_of_tea = 0
has_won = True

while bags_of_tea < 10:
    direction = input()
    a_row = alice_position[0] + possible_moves[direction][0]
    a_col = alice_position[1] + possible_moves[direction][1]

    if not (0 <= a_row < n and 0 <= a_col < n):
        has_won = False
        break

    alice_position = [a_row, a_col]

    if matrix[a_row][a_col] == "R":
        matrix[a_row][a_col] = "*"
        has_won = False
        break

    if matrix[a_row][a_col].isdigit():
        bags_of_tea += int(matrix[a_row][a_col])
    matrix[a_row][a_col] = "*"

if has_won:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
