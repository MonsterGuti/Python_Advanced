my_array = [3, 7, 11, 15, 19]

d = my_array[1] - my_array[0]
is_arithmetic = True

for i in range(2, len(my_array)):
    if my_array[i] - my_array[i - 1] != d:
        is_arithmetic = False
        break

if is_arithmetic:
    print(f'The array is an arithmetic progression with d = {d}.')
else:
    print('The array is not an arithmetic progression.')
