import math

number = int(input())

base = input()
if base == "natural":
    print(f'{math.log(number):.3f}')
else:
    print(f'{math.log(number, int(base)):.3f}')