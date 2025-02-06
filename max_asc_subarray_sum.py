from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        c = 0
        m = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                c += nums[i]
            else:
                m = max(c, m)
                c = nums[i]
        m = max(c, m)
        return m


s = Solution()
m = s.maxAscendingSum([12, 17, 15, 13, 10, 11, 12])
print(m)
