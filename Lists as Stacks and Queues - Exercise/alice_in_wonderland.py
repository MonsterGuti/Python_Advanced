n = int(input())
matrix = []
alice_position =

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":