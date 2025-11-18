arr = [
    [2, 3, 5, 7],
    [1, 4, 6, 8],
    [9, 10, 12, 11],
    [13, 14, 15, 16]
]

for row in arr:
    print(row)

my_arr = []
even_elements = 0
for i in range(len(arr)):
    if arr[i][i] % 2 == 0:
        my_arr.append(arr[i][i])
        even_elements += 1

negative_elements = 0
for i in range(len(arr)):
    if arr[i][len(arr) - i - 1] < 0:
        negative_elements += 1
        my_arr.append(arr[i][len(arr) - i - 1])

min_element_row = 0
min_element = None

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min_element:
            min_element = arr[i][j]
            min_element_row = i

max_element = 0
max_element_col = 0
first_iteration = True

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if first_iteration:
            max_element = arr[i][j]
            max_element_col = j
            first_iteration = False
        else:
            if arr[i][j] > max_element:
                max_element = arr[i][j]
                max_element_col = j
