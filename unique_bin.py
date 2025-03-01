from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        max_bin = "1" * len(nums)
        max_int = int(max_bin, 2)
        ints = set([i for i in range(max_int + 1)])
        bins = set([int(i, 2) for i in nums])
        ints -= bins
        return str(bin(list(ints)[0])[2:].zfill(len(nums)))
