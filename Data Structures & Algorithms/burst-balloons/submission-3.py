class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo: dict[tuple[int, int], int] = {}

        def dfs(l: int, r: int) -> int:
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            best = 0

            for last in range(l, r + 1):
                coins_from_last = nums[l - 1] * nums[last] * nums[r + 1]
                total = (
                    dfs(l, last - 1)
                    + coins_from_last
                    + dfs(last + 1, r)
                )
                best = max(best, total)
            
            memo[(l, r)] = best
            return best

        return dfs(1, len(nums) - 2)