def stats(*args):
    sum_negatives = sum(num for num in args if num < 0)
    sum_positives = sum(num for num in args if num > 0)
    result = f"{sum_negatives}\n{sum_positives}\n"

    if abs(sum_negatives) > sum_positives:
        result += "The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"

    return result


nums = [int(num) for num in input().split()]
print(stats(*nums))
