class Solution:
    def countDigitOne(self, n: int) -> int:
        c = 0
        i = 1
        while i <= n:
            d = i * 10
            c += (n // d) * i
            if (n % d) >= (i * 2):
                c += i
            elif (n % d) >= i:
                c += (n % d) - i + 1
            i *= 10

        return c


s = Solution()
print(s.countDigitOne(13))
