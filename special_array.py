from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def is_parity(a, b):
            return a % 2 == b % 2

        # f=True
        for i in range(len(nums) - 1):
            if is_parity(nums[i], nums[i + 1]):
                return False
        return True


sol = Solution()
print(sol.isArraySpecial([1, 2, 4, 4, 5]))
