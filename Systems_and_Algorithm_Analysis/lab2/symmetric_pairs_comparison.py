matrix = [
    [1, 3, 5],
    [7, 2, 4],
    [6, 8, 9]
]

n = len(matrix)

for i in range(n):
    for j in range(i + 1, n):
        upper = matrix[i][j]
        lower = matrix[j][i]
        if upper < lower:
            print(f"({i},{j}) = {upper} < ({j},{i}) = {lower}")
