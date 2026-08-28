class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n):
                b = nums[j]
                if j > i + 1 and b == nums[j - 1]:
                    continue
                
                l, r = j + 1, n - 1
                while l < r:
                    four_sum = a + b + nums[l] + nums[r]

                    if four_sum < target:
                        l += 1
                    elif four_sum > target:
                        r -= 1
                    else:
                        res.append([a, b, nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        r -= 1
                        while l < r and nums[r + 1] == nums[r]:
                            r -= 1

        return res                        