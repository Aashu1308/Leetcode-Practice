from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        if target < nums[l]:
            return 0
        if target > nums[r]:
            return n
        while l <= r:
            m = l + ((r - l) // 2)
            print(l, m, r)
            print(nums[l], nums[m], nums[r])
            if target == nums[m]:
                print("oop")
                return m
            elif target > nums[m]:
                print("whoop")
                l = m + 1
            else:
                print("doop")
                r = m - 1
        return l


s = Solution()
n = s.searchInsert([1, 3, 5, 6], 7)
print(n)
