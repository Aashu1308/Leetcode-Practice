from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        nums1 = nums + nums
        n = len(nums)
        current0s = total - sum(nums[:total])
        min_swaps = current0s
        for i in range(1, n):
            if nums1[i - 1] == 0:
                current0s -= 1
            if nums1[i + total - 1] == 0:
                current0s += 1
            min_swaps = min(min_swaps, current0s)
        return min_swaps


sol = Solution()
print(sol.minSwaps([1, 1, 0, 0, 1]))  # 1
