class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freq_count = [set() for _ in range(len(nums) + 1)]

        for n in nums:
            old_count = freq.get(n, 0)
            if old_count > 0:
                freq_count[old_count].remove(n)
            new_count = old_count + 1
            freq[n] = new_count
            freq_count[new_count].add(n)
        
        print(freq_count)
        c = 0
        res = []
        for count in range(len(freq_count) -1, -1, -1):
            print(count)

            for n in freq_count[count]:
                res.append(n) 
                c += 1
                print(n, c, k)
            if c == k:
                break
        
        return res



