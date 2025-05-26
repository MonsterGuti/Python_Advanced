number_of_names = int(input())
even_set = set()
odd_set = set()

for i in range(number_of_names):
    name = input()
    ascii_sum = sum(ord(char) for char in name)
    value = ascii_sum // (i + 1)

    if value % 2 == 0:
        even_set.add(value)
    else:
        odd_set.add(value)

sum_even = sum(even_set)
sum_odd = sum(odd_set)

if sum_even == sum_odd:
    print(*odd_set.union(even_set), sep=", ")
elif sum_odd > sum_even:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
