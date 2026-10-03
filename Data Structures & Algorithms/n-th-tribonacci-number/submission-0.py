class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def solve(x: int) -> int:
            if x == 0:
                memo[x] = 0
                return memo[x]
            elif x == 1 or x == 2:
                memo[x] = 1
                return memo[x]
            elif x in memo:
                return memo[x]
            else:
                prev_1 = solve(x - 1)
                prev_2 = solve(x - 2)
                prev_3 = solve(x - 3)

                memo[x] = prev_1 + prev_2 + prev_3
                return memo[x]

        return solve(n)