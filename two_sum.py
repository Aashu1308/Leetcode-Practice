class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = dict()
        for i, num in enumerate(nums):
            comp = target - nums[i]
            if comp in num_dict:
                return [num_dict[comp], i]
            num_dict[num] = i
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
