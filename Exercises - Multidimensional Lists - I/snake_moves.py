from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = deque(input())

matrix = []

for row in range(rows):
    current_row = []
    for _ in range(cols):
        current_row.append(snake[0])
        snake.rotate(-1)
    if row % 2 != 0:
        current_row.reverse()
    matrix.append(current_row)

for row in matrix:
    print("".join(row))
