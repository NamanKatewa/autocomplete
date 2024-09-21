class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence):
        words = sentence.split()
        for i in range(len(words)):
            current_node = self.root
            sub_sentence = " ".join(words[i:])
            for char in sub_sentence:
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
        return self._get_sentences_from_node(current_node, prefix)

    def _get_sentences_from_node(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, child_node in node.children.items():
            results.extend(self._get_sentences_from_node(child_node, prefix + char))
        return results


trie = Trie()

with open("sentences.txt", "r") as f:
    for line in f:
        sentence = line.strip()
        trie.insert(sentence)

while True:
    user_input = input("Enter a sentence prefix: ")
    suggestions = trie.search_prefix(user_input)
    print(suggestions)
