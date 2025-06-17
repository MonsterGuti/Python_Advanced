def find_factorial(num):
    if num == 1:
        return num
    return num * find_factorial(num - 1)

user_input = input()

print(find_factorial(int(user_input)))