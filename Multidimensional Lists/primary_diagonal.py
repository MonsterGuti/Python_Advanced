rows = int(input())
diagonal_sum = 0
matrix = []

for _ in range(rows):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

for row_index in range(rows):
    diagonal_sum += matrix[row_index][row_index]

print(diagonal_sum)