from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        k = 0
        for i in range(n):
            r = int(str(nums[i])[::-1])
            if nums[i] - r not in d:
                d[nums[i] - r] = 0
            d[nums[i] - r] += 1
        for i in d:
            k += (d[i] * (d[i] - 1)) // 2
        k %= (10**9) + 7
        print(k)
        return k
