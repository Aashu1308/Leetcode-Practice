from typing import List


class Solution:
    def trap(self, ls: List[int]) -> int:
        if not ls:
            return 0
        l = 0
        r = len(ls) - 1
        max_left = 0
        max_right = 0
        res = 0
        while l <= r:
            if ls[l] < ls[r]:
                if ls[l] >= max_left:
                    max_left = ls[l]
                res += max_left - ls[l]
                l += 1
            else:
                if ls[r] >= max_right:
                    max_right = ls[r]
                res += max_right - ls[r]
                r -= 1
        return res
