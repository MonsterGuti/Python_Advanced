def parse_input_line(line):
    return set(int(x.strip()) for x in line.split(",") if x.strip())

def cover_set(universe, sets):
    selected_sets = []
    while universe:
        best_set = max(sets, key=lambda s: len(universe.intersection(s)))
        selected_sets.append(best_set)
        universe -= best_set
        sets.remove(best_set)
    return selected_sets

universe = parse_input_line(input())
n = int(input())
sets = [parse_input_line(input()) for _ in range(n)]

selected = cover_set(universe, sets)

print(f"Sets to take ({len(selected)}):")
for s in selected:
    print(f"{{ {', '.join(map(str, sorted(s))) } }}")

