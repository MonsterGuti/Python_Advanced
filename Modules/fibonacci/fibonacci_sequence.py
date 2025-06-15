from Modules.fibonacci.fibonacci_module import create_sequence, locate

while True:
    command = input(">>> ")
    if command == "Stop":
        break
    elif command.startswith("Create Sequence"):
        try:
            number = int(command.split()[-1])
            fibonacci_sequence = create_sequence(number)
            print(*fibonacci_sequence)
        except ValueError:
            print("Invalid number.")
    elif command.startswith("Locate"):
        try:
            number = int(command.split()[-1])
            num_position = locate(number, fibonacci_sequence)
            print(num_position)
        except ValueError:
            print("Invalid number.")

            if num_position != -1:
                print(f'The number is at position {num_position}.")
            else:
                print("The number is not in the sequence.")
