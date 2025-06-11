symbols_to_replace = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            for symbol in symbols_to_replace:
                line = line.replace(symbol, "@")
            words = line.strip().split()
            reversed_words = words[::-1]
            print(" ".join(reversed_words))