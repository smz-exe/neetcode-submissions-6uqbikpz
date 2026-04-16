class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        n, m = len(A), len(B)
        total = n + m
        half = total // 2
        
        l, r = 0, n - 1
        while True:
            i = l + (r - l) // 2
            j = half - i - 2

            aLeftMax = A[i] if i >= 0 else float("-infinity")
            aRightMin = A[i + 1] if i + 1 < n else float("infinity")
            bLeftMax = B[j] if j >= 0 else float("-infinity")
            bRightMin = B[j + 1] if j + 1 < m else float("infinity")

            if aLeftMax <= bRightMin and aRightMin >= bLeftMax:
                if total % 2 == 1:
                    return min(aRightMin, bRightMin) 
                else:
                    return (max(aLeftMax, bLeftMax) + min(aRightMin, bRightMin)) / 2
            elif aLeftMax > bRightMin:
                    r = i - 1
            else:
                l = i + 1
            







