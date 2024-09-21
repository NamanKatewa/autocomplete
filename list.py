with open("words.txt", "r") as f:
    words = [line.strip() for line in f.readlines()]


def autocomplete(prefix):
    suggestions = [word for word in words if word.startswith(prefix)]
    return suggestions


prefix = input("Enter a word: ")
suggestions = autocomplete(prefix)
print(suggestions)
