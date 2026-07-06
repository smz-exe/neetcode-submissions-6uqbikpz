class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo: dict[tuple[int, int], int] = {}

        def dfs(left: int, right: int) -> int:
            if left > right:
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            best = 0
            for last in range(left, right + 1):
                coins_from_last = nums[left - 1] * nums[last] * nums[right + 1]
                total = (
                    dfs(left, last - 1)
                    + coins_from_last
                    + dfs(last + 1, right)
                )
                best = max(best, total)
            
            memo[(left, right)] = best
            return best
        
        return dfs(1, len(nums) - 2)
