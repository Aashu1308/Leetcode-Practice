from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1 for _ in nums]
        s = 1
        for i in range(1, len(nums)):
            p[i] = p[i - 1] * nums[i - 1]
        for i in range(len(nums) - 1, -1, -1):
            p[i] *= s
            s *= nums[i]
        return p
