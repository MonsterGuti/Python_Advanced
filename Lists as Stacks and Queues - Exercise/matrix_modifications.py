n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input().split()
    if command == "END":
        break
    r, c, value = command[1:]
    if r < 0 or r >= n or c < 0 or c > n:
        continue

    if command[0] == "Add":
        matrix[r][c] += value
    elif command[0] == "Subtract":
        matrix[r][c] -= value

[print(*row) for row in matrix]
