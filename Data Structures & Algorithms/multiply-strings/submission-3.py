class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n, m = len(num1), len(num2)
        acc = [0] * (n + m)

        for i in range(n):
            digit1 = ord(num1[n - 1 - i]) - ord("0")

            for j in range(m):
                digit2 = ord(num2[m - 1 - j]) - ord("0")
                acc[i + j] += digit1 * digit2
        
        for k in range(n + m - 1):
            acc[k + 1] += acc[k] // 10
            acc[k] %= 10
        
        while len(acc) > 1 and acc[-1] == 0:
            acc.pop()
        
        return "".join(chr(digit + ord("0")) for digit in reversed(acc))