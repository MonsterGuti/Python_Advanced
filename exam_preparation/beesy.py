class IncorrectWord(Exception):
    pass


def fix_position(bee_place, matrix_size):
    if bee_place[0] < 0:
        bee_place[0] = matrix_size - 1
    if bee_place[0] > matrix_size - 1:
        bee_place[0] = 0
    if bee_place[1] < 0:
        bee_place[1] = matrix_size - 1
    if bee_place[1] > matrix_size - 1:
        bee_place[1] = 0
    return bee_place


REQUIRED_HIVE_NECTAR = 30
initial_energy = 15

size = int(input())
matrix = []

mapper_position = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

bee_position = [0, 0]

for i in range(size):
    row = list(input())
    for j, ch in enumerate(row):
        if not (ch.isdigit() or ch in {'B', 'H', '-'}):
            raise IncorrectWord(f"Invalid character '{ch}' found.")
        if ch == "B":
            bee_position = [i, j]
    matrix.append(row)

collected_nectar = 0
is_revived = False

while initial_energy > 0:
    command = input()
    if command == "End":
        break
    if command not in mapper_position:
        continue

    new_row, new_col = mapper_position[command]
    next_position = [bee_position[0] + new_row, bee_position[1] + new_col]
    next_position = fix_position(next_position, size)
    initial_energy -= 1

    current_cell = matrix[next_position[0]][next_position[1]]

    if current_cell.isdigit():
        collected_nectar += int(current_cell)
        matrix[next_position[0]][next_position[1]] = "-"
    elif current_cell == "H":
        matrix[bee_position[0]][bee_position[1]] = "-"
        matrix[next_position[0]][next_position[1]] = "B"
        bee_position = next_position
        if collected_nectar >= REQUIRED_HIVE_NECTAR:
            print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    matrix[bee_position[0]][bee_position[1]] = "-"
    matrix[next_position[0]][next_position[1]] = "B"
    bee_position = next_position

    if initial_energy == 0:
        if collected_nectar > REQUIRED_HIVE_NECTAR and not is_revived:
            initial_energy = collected_nectar - REQUIRED_HIVE_NECTAR
            collected_nectar = REQUIRED_HIVE_NECTAR
            is_revived = True
        else:
            print("This is the end! Beesy ran out of energy.")
            break


[print(''.join(row)) for row in matrix]
