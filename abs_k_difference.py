from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d = {}
        c = 0
        for i in nums:
            if (i + k) in d:
                c += d[i + k]
            if (i - k) in d:
                c += d[i - k]
            if i not in d:
                d[i] = 0
            d[i] += 1
        return c
