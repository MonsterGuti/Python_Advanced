def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * power(x, n - 1)
    else:
        return 1 / pow(x, n - 1)

x = int(input())
n = int(input())
print(power(x, n))