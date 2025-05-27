from collections import deque

color_string = deque(input().split())

main_colors = ("red", "yellow", "blue")
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

collected_colors = []
collected_set = set()

while color_string:
    first_string = color_string.popleft()
    second_string = color_string.pop() if color_string else ""

    found_color = None
    for color in (first_string + second_string, second_string + first_string):
        if color in main_colors or color in secondary_colors:
            found_color = color
            break

    if found_color:
        if found_color not in collected_set:
            collected_colors.append(found_color)
            collected_set.add(found_color)
    else:
        if len(first_string) > 1:
            color_string.insert(len(color_string) // 2, first_string[:-1])
        if len(second_string) > 1:
            color_string.insert(len(color_string) // 2, second_string[:-1])

valid_colors = []
valid_set = set()

for color in collected_colors:
    if color in secondary_colors:
        if secondary_colors[color].issubset(collected_set):
            valid_colors.append(color)
            valid_set.add(color)
    else:
        valid_colors.append(color)
        valid_set.add(color)

print(valid_colors)
