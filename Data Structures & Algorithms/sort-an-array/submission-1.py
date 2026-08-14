class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr: list[int], left: int, mid: int, right: int) -> list[int]:
            left_arr = arr[left: mid + 1]
            right_arr = arr[mid + 1: right + 1]
            write, left_idx, right_idx = left, 0, 0

            while left_idx < len(left_arr) and right_idx < len(right_arr):
                if left_arr[left_idx] < right_arr[right_idx]:
                    arr[write] = left_arr[left_idx]
                    left_idx += 1
                else:
                    arr[write] = right_arr[right_idx]
                    right_idx += 1
                
                write += 1
            
            while left_idx < len(left_arr):
                arr[write] = left_arr[left_idx]
                left_idx += 1
                write += 1
            
            while right_idx < len(right_arr):
                arr[write] = right_arr[right_idx]
                right_idx += 1
                write += 1
            
            return arr


        def divide(arr: list[int], left: int, right: int):
            if left == right:
                return arr
            
            mid = left + (right - left) // 2
            divide(arr, left, mid)
            divide(arr, mid + 1, right)
            return merge(arr, left, mid, right)
        
        return divide(nums, 0, len(nums) - 1)
        
