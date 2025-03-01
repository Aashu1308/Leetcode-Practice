import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 2**31 - 1
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1
        return math.trunc(dividend / divisor)
