def sort_selection(numbers: list[int]) -> list[int]:
    for idx in range(len(numbers)):
        min_idx = idx
        for current_idx in range(idx+1, len(numbers)):
            if numbers[current_idx] < numbers[min_idx]:
                min_idx = current_idx
        numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]
    return numbers

numbers_list = [int(x) for x in input().split()]
print(*sort_selection(numbers_list))