def to_binary (num):
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    return to_binary(num // 2) + str(num % 2)

print(to_binary(10))
print(to_binary(100))