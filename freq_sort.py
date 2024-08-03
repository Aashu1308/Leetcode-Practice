from typing import List


class Solution:
    def __init__(self):
        self.freq_d = dict()

    def frequencySort(self, nums: List[int]) -> List[int]:
        for i in nums:
            if i not in self.freq_d:
                self.freq_d[i] = 0
            self.freq_d[i] += 1

        for i in range(len(nums)):
            swapped = False
            for j in range(0, len(nums) - i - 1):
                if self.compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums

    def compare(self, n1: int, n2: int) -> bool:
        try:
            if self.freq_d[n1] > self.freq_d[n2]:
                return True
            elif self.freq_d[n1] == self.freq_d[n2]:
                return n1 < n2
            else:
                return False
        except KeyError:
            return False


sol = Solution()
print(sol.frequencySort([2, 3, 1, 3, 2]))
