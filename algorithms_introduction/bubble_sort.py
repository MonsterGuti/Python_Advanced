def bubble_sort(numbers_list):
    is_sorted = False
    sorted_nums = 0
    while not is_sorted:
        is_sorted = True
        for j in range(1, len(numbers_list) - sorted_nums):
            i = j - 1
            if numbers_list[i] > numbers_list[j]:
                numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]
                is_sorted = False
        sorted_nums += 1
    return numbers_list


numbers = [int(x) for x in input().split()]
print(*bubble_sort(numbers))
