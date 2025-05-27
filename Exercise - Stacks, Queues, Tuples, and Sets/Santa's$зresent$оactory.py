from collections import deque

material_boxes = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

points = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
presents = {}

while material_boxes and magic_levels:
    total_magic = material_boxes[-1] * magic_levels[0]
    if total_magic in points:
        new_present = points[total_magic]
        if new_present not in presents:
            presents[new_present] = 0
        presents[new_present] += 1
        material_boxes.pop()
        magic_levels.popleft()
    elif total_magic < 0:
        new_material = material_boxes.pop() + magic_levels.popleft()
        material_boxes.append(new_material)
    elif total_magic > 0:
        magic_levels.popleft()
        material_boxes[-1] += 15
    else:
        if material_boxes[-1] == 0:
            material_boxes.pop()
        if magic_levels[0] == 0:
            magic_levels.popleft()

if ("Doll" in presents and "Wooden train" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_boxes:
    print(f"Materials left: {', '.join(str(x) for x in reversed(material_boxes))}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for key, value in sorted(presents.items()):
    print(f"{key}: {value}")
