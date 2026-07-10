class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        state = [False] * n
        state[n - 1] = True

        for i in range(n - 2, -1, -1):
            print(f"i: {i}")
            for j in range(i + nums[i], i - 1, -1):
                print(f"j: {j}")
                if j >= n or state[j]:
                    state[i] = True
                    break
            print(f"state[{i}]: {state[i]}")
        
        return state[0]