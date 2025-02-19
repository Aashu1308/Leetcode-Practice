class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        s = 0
        for i in str(num):
            s += int(i)
        if s < 10:
            return s
        return self.addDigits(s)
