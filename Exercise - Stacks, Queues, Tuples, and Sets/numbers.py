first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    command = input().split()
    action = command[0] + " " + command[1]
    numbers = [int(x) for x in command[2:]]

    if action == "Add First":
        first_sequence.update(numbers)
    elif action == "Add Second":
        second_sequence.update(numbers)
    elif action == "Remove First":
        first_sequence.difference_update(numbers)
    elif action == "Remove Second":
        second_sequence.difference_update(numbers)
    elif action == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
