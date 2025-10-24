N, K = map(int, input().split())
sheep_list = list(map(int, input().split()))
sheep_list.sort(reverse=True)
courses_min = max(sum(sheep_list) / K, max(sheep_list))
min_values_courses = []

sheep_index = 0
for course in range(K):
    current_course = 0
    while sheep_index < len(sheep_list):
        if current_course + sheep_list[sheep_index] <= courses_min:
            current_course += sheep_list[sheep_index]
            sheep_list.pop(sheep_index)
        else:
            sheep_index += 1
    min_values_courses.append(current_course)

for sheep in sheep_list:
    min_values_courses[min_values_courses.index(min(min_values_courses))] += sheep

print(max(min_values_courses))
