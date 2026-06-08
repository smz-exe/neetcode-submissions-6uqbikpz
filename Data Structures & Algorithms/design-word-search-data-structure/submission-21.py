class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_word = True

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(start: int, node: TrieNode) -> bool:
            if start == n:
                return node.is_word
            
            for i in range(start, n):
                char = word[i]

                if char == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
    
                    return False
                else:
                    if char not in node.children:
                        return False

                    node = node.children[char]  
            
            return node.is_word
        
        return dfs(0, self.root)
