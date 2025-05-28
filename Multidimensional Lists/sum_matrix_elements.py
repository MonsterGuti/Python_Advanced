row, cow = [int(x) for x in input().split(", ")]
matrix_sum = 0
matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split(", ")]
    matrix_sum += sum(row_data)
    matrix.append(row_data)

print(matrix_sum)
print(matrix)