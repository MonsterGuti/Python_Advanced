my_array = [3, -5, 7, -5, 3]

def recursive_sort(arr, n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    recursive_sort(arr, n - 1)

recursive_sort(my_array, len(my_array))
print("Sorted array:", my_array)

is_mirror = True
N = len(my_array)
for i in range(N // 2):
    a_val = my_array[i] if my_array[i] >= 0 else -my_array[i]
    b_val = my_array[N - 1 - i] if my_array[N - 1 - i] >= 0 else -my_array[N - 1 - i]
    if a_val != b_val:
        is_mirror = False
        break

if is_mirror:
    print("The array is mirror symmetric by absolute value.")
else:
    print("The array is NOT mirror symmetric by absolute value.")
