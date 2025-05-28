rows, cows = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)

max_sum = float('-inf')
sub_matrix = []

for row in range(rows - 1):
    for cow in range(cows - 1):
        current_num = matrix[row][cow]
        next_num = matrix[row][cow + 1]
        bellow_num = matrix[row + 1][cow]
        diagonal_num = matrix[row + 1][cow + 1]

        current_sum = current_num + next_num + bellow_num + diagonal_num
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_num, next_num],[bellow_num, diagonal_num]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
