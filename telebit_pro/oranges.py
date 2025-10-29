rows, cols, days = list(map(int, input().split()))
orange_matrix = []

for i in range(rows):
    orange_matrix.append([])
    for j in range(cols):
        orange_matrix[i].append(0)

for i in range(2):
    infected_row, infected_col = list(map(int, input().split()))
    orange_matrix[infected_row][infected_col] = 1

updated_orange_matrix = []
for row in range(rows):
    updated_orange_matrix.append(orange_matrix[row])


day = 1
while day <= days:
    for row in range(rows):
        for col in range(cols):
            if orange_matrix[row][col] == 1:
                if row < rows - 1:
                    updated_orange_matrix[row + 1][col] = 1
                if col < cols - 1:
                    updated_orange_matrix[row][col + 1] = 1
                if row > 0:
                    updated_orange_matrix[row - 1][col] = 1
                if col > 0:
                    updated_orange_matrix[row][col - 1] = 1
    day += 1

healthy_oranges = 0
for row in range(rows):
    for col in range(cols):
        if updated_orange_matrix[row][col] == 0:
            healthy_oranges += 1
print(updated_orange_matrix)
print(len(orange_matrix) * cols)
print(healthy_oranges)
