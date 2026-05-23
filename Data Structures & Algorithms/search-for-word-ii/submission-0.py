class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
    def add_word(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        root = TrieNode()
        for w in words:
            root.add_word(w)
        
        height, width = len(board), len(board[0])
        res = []
        visited = set()

        def dfs(r: int, c: int, node: TrieNode) -> None:
            out_of_bounds = r < 0 or c < 0 or r >= height or c >= width
            if (
                out_of_bounds
                or (r, c) in visited 
                or board[r][c] not in node.children
            ):
                return 
            
            ch = board[r][c]
            node = node.children[ch]

            if node.word is not None:
                res.append(node.word)
                node.word = None

            visited.add((r, c))

            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c -1, node)
            dfs(r, c + 1, node)

            visited.remove((r, c))
        
        for r in range(height):
            for c in range(width):
                dfs(r, c, root)
        
        return res

