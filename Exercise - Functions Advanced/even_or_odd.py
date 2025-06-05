def even_odd(*args):
    nums = list(args)
    command = nums.pop()

    if command == "even":
        return [num for num in nums if num % 2 == 0]
    elif command == "odd":
        return [num for num in nums if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
