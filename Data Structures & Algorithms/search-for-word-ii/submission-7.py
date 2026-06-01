class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.word: str | None = None
    
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
        
        rows, cols = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        res = []

        root = TrieNode()
        for word in words:
            root.add_word(word)

        def dfs(r: int, c: int, node: TrieNode) -> None:
            out_of_bounds = r < 0 or c < 0 or r >= rows or c >= cols

            if (
                out_of_bounds
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return
            
            ch = board[r][c]
            node = node.children[ch]
            visited.add((r, c))

            if node.word:
                res.append(node.word)
                node.word = None
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, node)
            
            visited.remove((r, c))
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return res
