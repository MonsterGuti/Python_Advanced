numbers_line = tuple([float(el) for el in input().split()])

numbers_dict = {}
for num in numbers_line:
    numbers_dict[num] = numbers_line.count(num)

for key, value in numbers_dict.items():
    print(f"{key} - {value} times")