from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cc = 1
        mx = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                cc += 1
                mx = max(mx, cc)
            else:
                cc = 1
        return max(mx, cc)


s = Solution()
print(f"op is {s.findLengthOfLCIS([2,2,2,2,2])}")
