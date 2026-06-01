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
        def dfs(i: int, node: TrieNode) -> bool:
            for idx in range(i, len(word)):
                c = word[idx]
   
                if c == ".":
                    for child in node.children.values():
                        if dfs(idx + 1, child):
                            return True

                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            
            return node.is_word
        
        return dfs(0, self.root)
                


                

