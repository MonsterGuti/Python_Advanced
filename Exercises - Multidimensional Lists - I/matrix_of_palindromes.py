rows, cols = [int(x) for x in input().split()]

starting_num = ord("a")

for row in range(rows):
    for col in range(cols):
        print(f"{chr(starting_num + row)}{chr(starting_num + row + 1)}{chr(starting_num + row)}", end=" ")
    print()