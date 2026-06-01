# I store all words in a Trie. For search, if the current character is normal,
# I follow the matching edges. If it is the wild card, I recursively try all children.
# At the end, I only return true if the current node is marked as a word.

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_word = True

    def search(self, word: str) -> bool:
        def dfs(start: int, node: TrieNode) -> bool:
            for i in range(start, len(word)):
                c = word[i]

                if c == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                if c not in node.children:
                    return False
                
                node = node.children[c]
            
            return node.is_word

        return dfs(0, self.root)
