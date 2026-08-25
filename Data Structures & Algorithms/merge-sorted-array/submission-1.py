class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def merge(arr: list[int], l: int, m: int, r: int):
            left = arr[l: m+1]
            right = arr[m+1: r+1]
            i, j = 0, 0
            k = l

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
                
        def merge_list(arr: list[int], l: int, r: int):
            if l == r:
                return
            
            m = l + (r - l) // 2
            merge_list(arr, l, m)
            merge_list(arr, m + 1, r)
            merge(arr, l, m, r)
        
        for i in range(len(nums2)):
            nums1[m + i] = nums2[i]

        merge_list(nums1, 0, len(nums1))

        
        