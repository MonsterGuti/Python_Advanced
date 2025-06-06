def fill_the_box(height, length, width, *args):
    v = height * length * width
    for cube in args:
        if cube == "Finish":
            break
        else:
            v -= cube
    if v >= 0:
        return f"There is free space in the box. You could put {v} more cubes."
    else:
        return f"No more free space! You have {abs(v)} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))