numbers_sum = 0

with open("numbers.txt") as f:
    for num in f:
        numbers_sum += int(num)

print(numbers_sum)
