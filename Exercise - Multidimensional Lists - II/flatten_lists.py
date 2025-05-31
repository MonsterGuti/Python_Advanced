user_input = input().split("|")
matrix = []

for i in range(len(user_input) - 1, -1, -1):
    nums = user_input[i].split()
    if nums:
        matrix.append(nums)

for row in matrix:
    print(*row, end=" ")