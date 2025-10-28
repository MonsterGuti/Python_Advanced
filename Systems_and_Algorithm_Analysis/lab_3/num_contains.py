def contains_digit(number, digit):
    if number == 0:
        return False
    if number % 10 == digit:
        return True
    return contains_digit(number // 10, digit)


number = int(input("Enter a number"))
digit = int(input("Enter a digit (0-9): "))

# Проверка и резултат
if contains_digit(number, digit):
    print(f"The digit {digit} is in {number}.")
else:
    print(f"The digit {digit} is not in {number}.")
