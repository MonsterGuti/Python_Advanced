my_arr = [24, 60, 36, 48, 12]

NOD = my_arr[0]
is_failed = False

for i in range(1, len(my_arr)):
    a = NOD
    b = my_arr[i]

    while b != 0:
        temp = b
        b = a % b
        a = temp

    NOD = a
    if NOD == 1:
        is_failed = True
        break

if not is_failed:
    print(my_arr)
    print(NOD)