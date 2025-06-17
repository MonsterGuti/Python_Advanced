def count_of_numbers(numbers, searched_num):
    right_idx = len(numbers) - 1
    left_idx = 0

    while right_idx >= left_idx:
        mid_idx = (right_idx + left_idx) // 2
        if numbers[mid_idx] == searched_num:
            return mid_idx
        if numbers[mid_idx] > searched_num:
            right_idx = mid_idx -1
        else:
            left_idx = mid_idx + 1

    return -1


nums = [int(x) for x in input().split()]
target_num = int(input())
print(count_of_numbers(nums, target_num))
