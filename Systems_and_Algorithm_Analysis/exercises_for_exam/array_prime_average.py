my_array = [2, 3, 4, 5, 6, 7, 8, 11]

sum_of_primes = 0
count_of_primes = 0

for num in my_array:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_of_primes += num
        count_of_primes += 1

avg_of_primes = sum_of_primes / count_of_primes
print(f'The average number of primes is: {avg_of_primes}.')
