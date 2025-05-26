words = set()

user_input = input()
for char in user_input:
    words.add(char)

for ch in sorted(words):
    print(f"{ch}: {user_input.count(ch)} time/s", sep="\n")