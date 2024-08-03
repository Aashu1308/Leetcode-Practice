from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # op=[i**2 for i in nums]
        # return sorted(op) #O(n log n)
        n = len(nums)
        ans = [0] * n
        left = 0
        right = n - 1
        index = n - 1
        while left <= right:
            l_2 = nums[left] ** 2
            r_2 = nums[right] ** 2
            if l_2 > r_2:
                ans[index] = l_2
                left += 1
            else:
                ans[index] = r_2
                right -= 1
            index -= 1
        return ans  # O(n)


sol = Solution()
print(sol.sortedSquares([-4, -1, 0, 3, 10]))
