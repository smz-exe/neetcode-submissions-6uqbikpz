class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx2 = len(numbers) - 1
        idx1 = idx2 - 1

        if (numbers[idx1] + numbers[idx2]) < target:
            return False
        
        hashmap = {}
        for i in range(len(numbers)):
            if numbers[i] in hashmap:
                return [ hashmap[numbers[i]]+1, i+1 ]
            else:
                hashmap[target - numbers[i]] = i
        return False
    