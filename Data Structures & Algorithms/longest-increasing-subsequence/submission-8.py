class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            l, r = 0, len(tails)
            while l < r:
                mid = l + (r - l) // 2

                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            
            if r == len(tails):
                tails.append(num)
            else:
                tails[r] = num
        
        return len(tails)