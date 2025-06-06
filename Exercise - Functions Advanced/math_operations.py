def math_operations(*args, **kwargs):
    operations = ["a", "s", "d", "m"]
    index = 0

    for num in args:
        key = operations[index % 4]

        if key == "a":
            kwargs[key] += num
        elif key == "s":
            kwargs[key] -= num
        elif key == "d":
            if num != 0:
                kwargs[key] /= num
        elif key == "m":
            kwargs[key] *= num
        index += 1
    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f"{k}: {v:.1f}" for k, v in sorted_items)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
