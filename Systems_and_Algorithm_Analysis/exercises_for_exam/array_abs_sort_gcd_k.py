my_arr = [12, 24, 36, -5, 7]
K = 3

for i in range(len(my_arr)):
    for j in range(i, len(my_arr)):
        val_a = my_arr[i] if my_arr[i] >= 0 else -my_arr[i]
        val_b = my_arr[j] if my_arr[j] >= 0 else -my_arr[j]
        if val_a > val_b:
            my_arr[i], my_arr[j] = my_arr[j], my_arr[i]

print(f"Sorted array is {my_arr}")

first_k = my_arr[:K]
print(f"First K elements: {first_k}")

NOD = first_k[0]

for i in range(1, len(first_k)):
    a = NOD
    b = first_k[i]

    while b != 0:
        temp = b
        b = a % b
        a = temp

    NOD = a

print(f'NOD is {NOD}')
