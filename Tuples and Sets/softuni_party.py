number_of_guests = int(input())
reservations = set()

for _ in range(number_of_guests):
    res_num = input()
    reservations.add(res_num)

while True:
    res = input()
    if res == "END":
        break
    reservations.remove(res)

print(len(reservations))
for res in sorted(reservations):
    print(res)