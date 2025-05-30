matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]
bomb_cells = input().split()

for cell in bomb_cells:
    row, col = [int(x) for x in cell.split(",")]
    bomb_value = matrix[row][col]
    if bomb_value <= 0:
        continue
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < matrix_size and 0 <= c < matrix_size and (r != row or c != col):
                if matrix[r][c] > 0:
                    matrix[r][c] -= bomb_value

    matrix[row][col] = 0

alive_cells = [cell for row in matrix for cell in row if cell > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(" ".join(str(x) for x in row)) for row in matrix]