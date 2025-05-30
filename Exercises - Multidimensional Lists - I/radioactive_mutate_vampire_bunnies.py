def spread_bunnies(mat, bunnies_set):
    new_bunnies_set = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for b_row, b_col in bunnies_set:
        for d_row, d_col in directions:
            new_row, new_col = b_row + d_row, b_col + d_col
            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]):
                mat[new_row][new_col] = "B"
                new_bunnies_set.add((new_row, new_col))

    return mat, bunnies_set.union(new_bunnies_set)


rows, cols = [int(x) for x in input().split()]

matrix = []
p_row, p_col = 0, 0
bunnies = set()

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == "P":
            p_row, p_col = row, col
        elif matrix[row][col] == "B":
            bunnies.add((row, col))

commands = list(input())

has_won = False
has_lost = False

moves = {
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c),
    "L": lambda r, c: (r, c - 1),
    "R": lambda r, c: (r, c + 1)
}

for command in commands:
    new_player_row, new_player_col = moves[command](p_row, p_col)
    matrix, bunnies = spread_bunnies(matrix, bunnies)
    if (p_row, p_col) not in bunnies:
        matrix[p_row][p_col] = "."

    if new_player_row < 0 or new_player_row >= rows or new_player_col < 0 or new_player_col >= cols:
        has_won = True
        break

    p_row, p_col = new_player_row, new_player_col
    if matrix[p_row][p_col] == "B":
        has_lost = True
        break

for row in matrix:
    print("".join(row))

if has_won:
    print(f"won: {p_row} {p_col}")
if has_lost:
    print(f"dead: {p_row} {p_col}")