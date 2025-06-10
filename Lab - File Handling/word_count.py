from collections import Counter
import re

with open("words.txt") as words_file:
    target_words = words_file.read().split()
    target_words = [word.lower() for word in target_words]

with open("text.txt") as text_file:
    text = text_file.read().lower()
    words_in_text = re.findall(r"\b\w+\b", text)

word_counter = Counter(words_in_text)

result = {word: word_counter[word] for word in target_words}
sorted_result = sorted(result.items(), key=lambda x: -x[1])

with open("output.txt", "w") as output_file:
    for word, count in sorted_result:
        output_file.write(f"{word} - {count}\n")
