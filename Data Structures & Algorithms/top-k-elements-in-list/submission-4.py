class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(set(nums))

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0) 

        freq = []
        for (num, value) in count.items():
            freq.append((value, num))
        freq.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(freq[i][1])
        return res

        


        

