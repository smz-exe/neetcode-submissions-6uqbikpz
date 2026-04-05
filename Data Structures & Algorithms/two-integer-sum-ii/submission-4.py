class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i+1, len(numbers) - 1
            temp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if temp == numbers[mid]:
                    return [ i+1, mid+1 ]
                elif temp > numbers[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return []

    