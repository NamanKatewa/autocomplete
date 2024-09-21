class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search_prefix(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]
        return self._get_words_from_node(current_node, prefix)

    def _get_words_from_node(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, child_node in node.children.items():
            results.extend(self._get_words_from_node(child_node, prefix + char))
        return results


trie = Trie()
with open("words.txt", "r") as f:
    for line in f:
        word = line.strip()
        trie.insert(word)


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def combined_autocomplete(prefix, max_distance=2):
    trie_suggestions = trie.search_prefix(prefix)

    if len(trie_suggestions) < 5:
        with open("words.txt", "r") as f:
            words = [line.strip() for line in f.readlines()]
        levenshtein_suggestions = [
            word for word in words if levenshtein_distance(prefix, word) <= max_distance
        ]

        return list(set(trie_suggestions + levenshtein_suggestions))

    return trie_suggestions


user_input = input("Enter a word: ")
suggestions = combined_autocomplete(user_input)
print("Suggestions:", suggestions)
