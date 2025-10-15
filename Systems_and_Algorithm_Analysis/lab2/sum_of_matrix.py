def sum_border_elements(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total = 0

    total += sum(matrix[0])

    if rows > 1:
        total += sum(matrix[rows - 1])

    for i in range(1, rows - 1):
        total += matrix[i][0]
        total += matrix[i][cols - 1]

    return total


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

result = sum_border_elements(matrix)
print("sum of elements in the orbit: ", result)
