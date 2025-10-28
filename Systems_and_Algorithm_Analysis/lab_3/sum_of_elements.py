def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sum_array(arr, n - 1)


arr = [int(x) for x in input("enter the elements of the array").split()]

result = sum_array(arr, len(arr))

print(f"the sum is {result}")
