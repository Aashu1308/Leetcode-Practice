class Solution:
    def isHappy(self, n: int) -> bool:
        c = 0
        while n != 1 and c < 20:
            s = 0
            for i in str(n):
                s += int(i) ** 2
            n = s
            c += 1
        return n == 1
