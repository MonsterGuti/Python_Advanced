def age_assignment(*args, **kwargs):
    result = ""
    sorted_info = sorted(kwargs.items(), key=lambda x: x[0])
    for letter, age in sorted_info:
        for name in args:
            if name.startswith(letter):
                result += f"{name} is {age} years old.\n"
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))