chemicals = set()

for _ in range(int(input())):
    chemical_line = input().split()
    for chemical in chemical_line:
        chemicals.add(chemical)

print(*chemicals, sep="\n")