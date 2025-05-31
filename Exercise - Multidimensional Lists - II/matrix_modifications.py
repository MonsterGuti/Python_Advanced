n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    r, c, value = map(int, command[1:])

    if 0 <= r < n and 0 <= c < n:
        if command[0] == "Add":
            matrix[r][c] += value
        elif command[0] == "Subtract":
            matrix[r][c] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)
