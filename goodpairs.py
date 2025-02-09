from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        k = 0
        t = (n * (n - 1)) // 2
        for i in range(n):
            if nums[i] - i not in d:
                d[nums[i] - i] = 0
            d[nums[i] - i] += 1
        for i in d:
            k += (d[i] * (d[i] - 1)) // 2
        print(t, k)
        return t - k
