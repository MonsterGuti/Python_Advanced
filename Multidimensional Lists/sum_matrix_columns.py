rows, cows = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for cow in range(cows):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][cow]
    print(current_sum, end="\n")
