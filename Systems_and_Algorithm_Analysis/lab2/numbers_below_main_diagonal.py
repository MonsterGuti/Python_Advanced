rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the matrix row by row:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

result = []

diagonal_sum = 0
for i in range(min(rows, cols)):
    diagonal_sum += matrix[i][i]
result.append(diagonal_sum)

for i in range(rows):
    row_sum = sum(matrix[i])
    result.append(row_sum)

count = 0
for i in range(rows):
    for j in range(cols):
        if i > j and matrix[i][j] < i + j:
            count += 1
result.append(count)

print("Result array:")
print(result)
