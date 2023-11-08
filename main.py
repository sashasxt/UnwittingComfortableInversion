# подготовка текста к анализу

text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

# анализ текста

char_frequency = {}

for char in text:
    # частота символов считается тут
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

shorter_word = words[0]

for word in words:
    if len(word) < len(shorter_word):
        shorter_word = word

# вывод результатов

print("Количество разных слов:", len(set(words)))
print("Самое длинное слово:", longest_word)
print("Самое короткое слово:", shorter_word)

print("Частота символов:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")