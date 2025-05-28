rows = int(input())
matrix = []

for _ in range(rows):
    row_data = [char for char in input()]
    matrix.append(row_data)

searched_symbol = input()

for row in range(rows):
    for cow in range(rows):
        if searched_symbol == matrix[row][cow]:
            print(f"({row}, {cow})")
            exit()

print(f"{searched_symbol} does not occur in the matrix")