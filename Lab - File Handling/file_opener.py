try:
    with open("text.txt") as file:
        print("File found")
except FileExistsError:
    print("File not found")
