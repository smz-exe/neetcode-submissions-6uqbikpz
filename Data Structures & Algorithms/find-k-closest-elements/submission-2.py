class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = -1, -1

        for i in range(len(arr)):
            if arr[i] >= x:
                if i - 1 >= 0 and abs(x - arr[i - 1]) <= abs(x - arr[i]):
                    l, r = i - 1, i - 1
                else:
                    l, r = i, i

                break
        
        if l == -1:
            l, r = len(arr) - 1, len(arr) - 1

        while (r - l + 1) < k:
            if l <= 0:
                r += 1
            elif r >= len(arr) - 1:
                l -= 1
            elif abs(x - arr[l - 1]) <= abs(x - arr[r + 1]):
                l -= 1
            else:
                r += 1

        return arr[l : r + 1]
