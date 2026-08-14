class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr: list[int], left: int, mid: int, right: int) -> list[int]:
            left_arr = arr[left: mid + 1]
            right_arr = arr[mid + 1: right + 1]
            i, j, k = left, 0, 0

            while j < len(left_arr) and k < len(right_arr):
                if left_arr[j] < right_arr[k]:
                    arr[i] = left_arr[j]
                    j += 1
                else:
                    arr[i] = right_arr[k]
                    k += 1
                
                i += 1
            
            while j < len(left_arr):
                arr[i] = left_arr[j]
                j += 1
                i += 1
            
            while k < len(right_arr):
                arr[i] = right_arr[k]
                k += 1
                i += 1
            
            return arr


        def devide(arr: list[int], left: int, right: int):
            if left == right:
                return arr
            
            mid = left + (right - left) // 2
            devide(arr, left, mid)
            devide(arr, mid + 1, right)
            return merge(arr, left, mid, right)
        
        return devide(nums, 0, len(nums) - 1)
        
