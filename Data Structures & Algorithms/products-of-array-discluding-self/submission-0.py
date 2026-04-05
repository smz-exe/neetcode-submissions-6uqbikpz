class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = 1
        numOfZero = 0
        for num in nums:
            if num == 0:
                numOfZero += 1
            else:
                products *= num
        
        res = []
        if numOfZero >= 2:
            res = [0 for _ in range(len(nums))]
        elif numOfZero == 1:
            for n in nums:
                if n == 0:
                    res.append(products)
                else:
                    res.append(0)
        else:
            for n in nums:
                res.append(products//n)
        return res