class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(idx: int, node: TrieNode) -> bool:
            for i in range(idx, len(word)):
                c = word[i]

                if c ==".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]

            return node.is_end
        
        return dfs(0, self.root)