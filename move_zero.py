from typing import List


class Solution:
    def moveZeroes(self, ls: List[int]) -> None:
        l = 0
        for i in range(len(ls)):
            if ls[i] != 0:
                ls[l], ls[i] = ls[i], ls[l]
                l += 1
        return ls
