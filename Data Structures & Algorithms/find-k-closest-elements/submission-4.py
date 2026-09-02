class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            mid = l + (r - l) // 2

            if abs(x - arr[mid]) > abs(x - arr[mid + k]):
                l = mid + 1
            else:
                r = mid

        return arr[l : l + k]
