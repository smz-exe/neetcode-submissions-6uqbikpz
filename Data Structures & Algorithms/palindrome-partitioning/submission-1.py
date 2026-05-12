class Solution:
# pattern: DP preprocessing + backtracking
# data structure:
#   - pals[l][r]: whether s[l:r+1] is a palindrome
#   - part: current palindrome partition
#   - res: all valid partitions
# main invariant:
#   - dfs(i) partitions the suffix s[i:]
#   - all strings in part are palindromes
#   - part concatenated with s[i:] represents the original string prefix/suffix split
# edge cases:
#   - single-character substrings are always palindromes
#   - length-2 substrings need direct character comparison
#   - strings with many repeated characters generate many partitions
# time complexity: O(n^2 + n * 2^n)
# space complexity: O(n^2 + n), excluding output

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        pals = [[False for _ in range(n)] for _ in range(n)]
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if length == 1:
                    pals[l][r] = True
                elif length == 2:
                    if s[l] == s[r]:
                        pals[l][r] = True
                else:
                    if s[l] == s[r]:
                        pals[l][r] = pals[l + 1][r - 1]

        res = []
        part = []

        def dfs(i: int) -> None:
            if i >= n:
                res.append(part.copy())
                return
            
            for j in range(i, n):
                if pals[i][j]:
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()        

        dfs(0)
        return res