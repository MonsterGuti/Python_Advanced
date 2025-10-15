n = int(input("Enter the size of the square matrix: "))

matrix = []
print("Enter the matrix row by row:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

secondary_sum = 0
for i in range(n):
    secondary_sum += matrix[i][n - 1 - i]

print("Sum of the secondary diagonal elements:", secondary_sum)
