first_set = set()
second_set = set()

n, m = (int(x) for x in input().split())

for _ in range(n):
    first_set.add(input())
for _ in range(m):
    second_set.add(input())

print(*(first_set.intersection(second_set)), sep="\n")