from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = Counter(nums)
        maxfreq = max(freqs.values())
        count = 0
        for i in freqs.keys():
            if freqs[i] == maxfreq:
                count += 1
        return count * maxfreq


sol = Solution()
print(sol.maxFrequencyElements([1, 2, 2, 2, 3, 3, 3]))  # 3
