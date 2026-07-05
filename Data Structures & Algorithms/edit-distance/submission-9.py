class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        prev = [m - j for j in range(m + 1)]

        for i in range(n - 1, -1, -1):
            cur = [0] * (m + 1)
            cur[m] = n - i

            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    cur[j] = prev[j + 1]
                else:
                    candidates = (
                        1 + cur[j + 1],
                        1 + prev[j],
                        1 + prev[j + 1]
                    )
                    cur[j] = min(candidates)

            prev = cur

        return prev[0]