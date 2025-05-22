clothes_in_box = list(map(int, input().split()))
rack_capacity = int(input())
rack_number = 1
current_sum = 0

while clothes_in_box:
    clothing = clothes_in_box.pop()
    if current_sum + clothing > rack_capacity:
        rack_number += 1
        current_sum = clothing
    else:
        current_sum += clothing

print(rack_number)
