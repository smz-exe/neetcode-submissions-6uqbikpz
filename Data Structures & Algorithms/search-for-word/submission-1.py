class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        path = set()

        def dfs(i: int, pt: tuple[int, int]) -> bool:
            if i == len(word):
                return True
            
            r, c = pt[0], pt[1]

            if (r < 0 or c < 0 or
                r >= h or c >= w or
                (r, c) in path or board[r][c] != word[i]):
                return False
            
            path.add((r, c))
            res = (dfs(i + 1, (r + 1, c)) or
                    dfs(i + 1, (r - 1, c)) or 
                    dfs(i + 1, (r, c + 1)) or 
                    dfs(i + 1, (r, c - 1)))
            path.remove((r, c))
            return res
        
        for i in range(h):
            for j in range(w):
                if  dfs(0, (i, j)):
                    return True

        return False        
        
