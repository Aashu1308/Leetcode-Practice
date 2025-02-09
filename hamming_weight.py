class Solution:
    def hammingWeight(self, n: int) -> int:
        b_str = str(bin(n))
        s = 0
        for i in b_str[2:]:
            s += int(i)
        return s
