class Solution:
    def reverse(self, x: int) -> int:
        sx = str(abs(x))
        sign = lambda s: "" if s > 0 else "-"
        sn = sign(x)
        sol = int(sn + sx[::-1])
        if sol > 2**31 - 1 or sol < -(2**31):
            return 0
        return sol


sol = Solution()
print(sol.reverse(15623))
print(sol.reverse(-123))
