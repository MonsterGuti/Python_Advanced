rows, cols = (int(x) for x in input().split())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

my_sum = -float('inf')
max_row = 0
max_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        for r in range(rows, rows + 3):
            for c in range(cols, cols + 3):
                current_sum += matrix[r][c]
        if current_sum > my_sum:
            my_sum = current_sum
            max_row = row
            max_col = col

print(f"Sum = {my_sum}")
max_matrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in matrix]