from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        c = 0
        r = len(nums) - 1
        if len(nums) == 0:
            return 0
        print(r)
        while r >= 0 and nums[r] == val:
            r -= 1
            c += 1
        if r < 0:
            return 0
        while l <= r:
            # print(l, r, nums[l], nums[r])
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                c += 1
                while r >= 0 and nums[r] == val:
                    r -= 1
                    c += 1
                if r < 0:
                    break
            else:
                l += 1
        return len(nums) - c


s = Solution()
nums = [1]
print(s.removeElement(nums, 1))
print(nums)
