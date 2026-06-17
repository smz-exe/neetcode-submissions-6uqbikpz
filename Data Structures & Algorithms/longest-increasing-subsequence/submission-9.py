class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        
        for num in nums:
            l, r = 0, len(tails)

            while l < r:
                mid = l + (r - l) // 2

                if num > tails[mid]:
                    l = mid + 1
                else:
                    r = mid
            
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num
        
        return len(tails)