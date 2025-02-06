from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        for i in range(len(nums)):
            if i != len(nums) - 1:
                if nums[i] > nums[i + 1]:
                    c += 1
                    print(nums[i], nums[i + 1])
            else:
                if nums[i] > nums[0]:
                    c += 1
                    print(nums[i], nums[0])
        # print(c)
        return c >= 1


s = Solution()
print(s.check([3, 4, 5, 1, 2]))  # True
