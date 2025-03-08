from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cc = 0
        mx = 0
        for i in nums:
            if i == 1:
                cc += 1
                if mx < cc:
                    mx = cc
            else:
                cc = 0
        return mx


s = Solution()
print(f"op is {s.findMaxConsecutiveOnes([1,1,0,1,1,1])}")
print(f"op is {s.findMaxConsecutiveOnes([1,0,1,1,0,1])}")
