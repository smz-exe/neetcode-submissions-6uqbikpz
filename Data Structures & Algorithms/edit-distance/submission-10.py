class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        below = [m - j for j in range(m + 1)]

        for i in range(n - 1, -1, -1):
            current = [0] * (m + 1)
            current[m] = n - i

            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    current[j] = below[j + 1]
                else:
                    candidates = (
                        1 + current[j + 1],
                        1 + below[j],
                        1 + below[j + 1]
                    )
                    current[j] = min(candidates)

            below = current

        return below[0]