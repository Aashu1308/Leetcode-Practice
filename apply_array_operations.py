from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        nz = [i for i in nums if i != 0]
        nz += [0] * (len(nums) - len(nz))
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == 0:
        #             nums[i], nums[j] = nums[j], nums[i]
        return nz


s = Solution()
print(s.applyOperations([1, 2, 2, 1, 1, 0]))
print(s.applyOperations([0, 1]))
