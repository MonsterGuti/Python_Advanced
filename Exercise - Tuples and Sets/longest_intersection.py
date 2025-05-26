def create_set_from_range(range_str):
    start, end = (int(x) for x in range_str.split(","))
    return set(range(start, end + 1))


longest_intersection = set()
n = int(input())

for _ in range(n):
    first_range, second_range = input().split("-")

    first_set = create_set_from_range(first_range)
    second_set = create_set_from_range(second_range)
    intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
longest_intersection = list(longest_intersection)
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")