class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.word: str | None = None
    
    def add_word(self, word: str) -> None:
        cur = self

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
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
            char = board[r][c]
            node = node.children[char]
            visited.add((r, c))

            if node.word:
                res.append(node.word)
                node.word = None
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and board[nr][nc] in node.children
                ):
                    dfs(nr, nc, node)
            
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                if (
                    board[r][c] in root.children
                ):
                    dfs(r, c, root)
        
        return res