from typing import List


def remove_duplicates(nums: List[int]) -> int:
    ln = len(nums) - 1
    n = 0
    for _ in range(ln):
        if nums[n] == nums[n + 1]:
            nums[n + 1 :] = nums[n + 2 :]
            n -= 1
        n += 1
    if len(nums) == 2 and nums[0] == nums[1]:
        nums[:] = []


nums = [1, 2, 2]
print(len(nums))
remove_duplicates(nums)
print(nums)
print(len(nums))
