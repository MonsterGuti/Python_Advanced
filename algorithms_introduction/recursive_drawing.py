def draw_figure(num):
    if num <= 0:
        return 0
    print("*" * num)

    draw_figure(num - 1)

    print("#" * num)


number = int(input())
draw_figure(number)
