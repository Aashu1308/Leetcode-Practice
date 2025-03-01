class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        fmin = nums[0]
        fmax = nums[0]
        max_s = 0
        min_s = 0
        for i in range(len(nums)):
            max_s += nums[i]
            min_s += nums[i]
            if max_s < 0:
                max_s = 0
            if min_s > 0:
                min_s = 0
            fmax = max(fmax, max_s)
            fmin = min(fmin, min_s)
        return max(fmax, abs(fmin))
