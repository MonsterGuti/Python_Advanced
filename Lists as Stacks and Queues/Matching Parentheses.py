user_input = list(input())
stack = []

for i in range(len(user_input)):
    if user_input[i] == "(":
        stack.append(i)
    elif user_input[i] == ")":
        start_index = stack.pop()
        end_index = i + 1
        print("".join(user_input[start_index:end_index]))

