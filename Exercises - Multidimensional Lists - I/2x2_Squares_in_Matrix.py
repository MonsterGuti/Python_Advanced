rows, cols = (int(x) for x in input().split())
matrix = [input().split() for _ in range(rows)]
found_matrix = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            found_matrix += 1

print(f"{found_matrix}")