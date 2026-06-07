class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        arr = nums[:]
        arr.append(0)

        if n == 1:
            return nums[0]

        for i in range(n - 3, -1, -1):
            arr[i] = arr[i] + max(arr[i + 2], arr[i + 3])
        
        return max(arr[0], arr[1])