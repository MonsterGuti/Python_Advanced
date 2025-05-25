number_of_students = int(input())
students_info = {}

for _ in range(number_of_students):
    line = tuple(input().split())
    name, grade = line
    grade = float(grade)
    if name not in students_info:
        students_info[name] = []
    students_info[name].append(grade)

for key, value in students_info.items():
    print(f"{key} -> {' '.join(f'{v:.2f}' for v in value)} (avg: {(sum(value)/len(value)):.2f})")