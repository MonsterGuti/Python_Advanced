n = int(input())

matrix = []
bunny = []

for row in range(n):
    matrix.append(input().split())
    for cow in range(n):
        if matrix[row][cow] == "B":
            bunny = [row, cow]

possible_moves = {"down": (1, 0), "up": (-1, 0), "right": (0, 1), "left": (0, -1)}
max_position = ""
max_eggs_matrix = []
max_eggs = float('-inf')

for direction, move in possible_moves.items():
    eggs = 0
    egg_matrix = []
    b_row = bunny[0] + move[0]
    b_col = bunny[1] + move[1]

    while 0 <= b_row < n and 0 <= b_col < n:
        if matrix[b_row][b_col] == "X":
            break
        eggs += int(matrix[b_row][b_col])
        egg_matrix.append([b_row, b_col])
        b_row += move[0]
        b_col += move[1]

    if eggs > max_eggs:
        max_eggs = eggs
        max_eggs_matrix = egg_matrix
        max_position = direction

print(max_position)
[print(row) for row in max_eggs_matrix]
print(max_eggs)
