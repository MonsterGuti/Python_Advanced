sequence_of_parentheses = input()

parentheses = {"(": ")", "[": "]", "{": "}"}
stack = []

for char in sequence_of_parentheses:
    if char in parentheses:
        stack.append(char)
    elif char in parentheses.values():
        if not stack:
            print("NO")
            break
        last_opening_parethesis = stack.pop()
        if parentheses[last_opening_parethesis] != char:
            print("NO")
            break
else:
    if stack:
        print("NO")
    else:
        print("YES")