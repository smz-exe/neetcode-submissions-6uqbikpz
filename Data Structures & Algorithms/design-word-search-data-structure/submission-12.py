class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.is_word = True

    def search(self, word: str) -> bool:

        def dfs(idx: int, node: TrieNode) -> bool:
            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False        
                else:
                    if not c in node.children:
                        return False
                    node = node.children[c]
            
            return node.is_word

        return dfs(0, self.root)
