class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A # len(A) <= len(B)
        n, m = len(A), len(B)
        total = n + m
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            i = l + (r - l) // 2
            j = half - i - 2

            leftA = A[i] if i >= 0 else float("-infinity")
            rightA = A[i+1] if i + 1 < n else float("infinity")
            leftB = B[j] if j >= 0 else float("-infinity")
            rightB = B[j+1] if j + 1 < m else float("infinity")

            print(n, m)
            print(i, j)
            print(leftA, rightA)
            print(leftB, rightB)
            print("\n")
            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1
