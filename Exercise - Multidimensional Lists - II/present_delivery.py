total_presents = int(input())
n = int(input())
matrix = []
santa = [0, 0]
initial_nice_kids = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            initial_nice_kids += 1

nice_kids_without_present = initial_nice_kids
total_nice_kids = initial_nice_kids

possible_moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

while True:
    direction = input()
    if direction == "Christmas morning" or total_presents == 0:
        break

    r = santa[0] + possible_moves[direction][0]
    c = santa[1] + possible_moves[direction][1]

    if not (0 <= r < n and 0 <= c < n):
        break

    matrix[santa[0]][santa[1]] = "-"
    santa = [r, c]

    if matrix[r][c] == "V":
        total_presents -= 1
        nice_kids_without_present -= 1
    elif matrix[r][c] == "C":
        for move in possible_moves.values():
            nr, nc = r + move[0], c + move[1]
            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] in "VX":
                if matrix[nr][nc] == "V":
                    nice_kids_without_present -= 1
                matrix[nr][nc] = "-"
                total_presents -= 1
                if total_presents == 0:
                    break

    matrix[r][c] = "S"

    if total_presents == 0:
        break

if total_presents == 0 and nice_kids_without_present > 0:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if nice_kids_without_present == 0:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_without_present} nice kid/s.")
