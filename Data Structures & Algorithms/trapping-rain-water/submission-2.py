class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)

        hashmap = {}

        l, r = 0, 1
        while l < n and r < n:
            area = 0
            while r < n and height[l] > height[r]:
                area += height[l] - height[r]
                r += 1
            if r < n:
                hashmap[(l, r)] = area
            l, r = r, r + 1


        r, l = n - 1, n - 2
        while r >= 0 and l >= 0:
            area = 0
            while l >=0 and height[l] < height[r]:
                area += height[r] - height[l]
                l -= 1
            if l >= 0:
                hashmap[(l, r)] = area
            l, r = l - 1, l

        for v in hashmap.values():
            res += v
        return res

