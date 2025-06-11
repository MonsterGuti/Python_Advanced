from string import punctuation

with open("text.txt") as input_file, open("output.txt", "w") as output_file:
    result = []

    for r, line in enumerate(input_file):
        letters_count = 0
        punctuation_count = 0
        for char in line:
            if char.isalpha():
                letters_count += 1
            elif char in punctuation:
                punctuation_count += 1
        result.append(f"Line {r + 1}: {line.strip()} ({letters_count})({punctuation_count})")

    output_file.write("\n".join(result))
