class Solution:
    def __init__(self):
        pass
    def concatHex36(self, n: int) -> str:
        num = n**2
        rem = num % 16
        res = self.convert(rem)
        num = num // 16
        while num != 0:
            res += self.convert(num%16)
            num //= 16
        num = n ** 3
        while num != 0:
            res += self.convert(num % 36)
            num //= 36
        return res
    def convert(self, num):
        m = 0
        if num > 9:
            m = ord('A') + num - 10
            return chr(m)
        return str(num)
x = Solution()
print(x.concatHex36(4))
