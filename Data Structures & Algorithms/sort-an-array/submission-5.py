class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr: list[int], left: int, mid: int, right: int) -> None:
            arr_left = arr[left: mid + 1]
            arr_right = arr[mid + 1: right + 1]
            idx, idx_l, idx_r = left, 0, 0

            while idx_l < len(arr_left) and idx_r < len(arr_right):
                if arr_left[idx_l] <= arr_right[idx_r]:
                    nums[idx] = arr_left[idx_l]
                    idx_l += 1
                else:
                    nums[idx] = arr_right[idx_r]
                    idx_r += 1
                
                idx += 1
            
            while idx_l < len(arr_left):
                nums[idx] = arr_left[idx_l]
                idx_l += 1
                idx += 1
            
            while idx_r < len(arr_right):
                nums[idx] = arr_right[idx_r]
                idx_r += 1
                idx += 1

        def merge_sort(arr: list[int], left: int, right: int):
            if left >= right:
                return
            
            mid = left + (right - left) // 2

            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)
            merge(arr, left, mid, right)
        
        merge_sort(nums, 0, len(nums) - 1)
        return nums

