class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        MIN_Q = int(MIN / 10)
        MIN_R = int(math.fmod(MIN, 10))
        MAX_Q = MAX // 10
        MAX_R = MAX % 10

        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (
                res < MIN_Q
                or (res == MIN_Q and digit < MIN_R)
            ):
                return 0
            
            if (
                res > MAX_Q
                or (res == MAX_Q and digit > MAX_R)
            ):
                return 0

            res = (res * 10) + digit

        return res