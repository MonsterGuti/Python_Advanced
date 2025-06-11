import os

while True:
    command = input()
    if command == "End":
        break

    parts = command.split("-")
    action = parts[0]
    file_name = parts[1]

    if action == "Create":
        with open(file_name, "w") as f:
            pass

    elif action == "Add":
        content = parts[2]
        with open(file_name, "a") as f:
            f.write(content + "\n")

    elif action == "Replace":
        old_string = parts[2]
        new_string = parts[3]
        if not os.path.exists(file_name):
            print("An error occurred")
        else:
            with open(file_name, "r") as f:
                text = f.read()
            text = text.replace(old_string, new_string)
            with open(file_name, "w") as f:
                f.write(text)

    elif action == "Delete":
        if not os.path.exists(file_name):
            print("An error occurred")
        else:
            os.remove(file_name)
