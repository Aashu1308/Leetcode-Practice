from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        r = len(grid)
        r = r * r + 1
        f = {}
        for i in grid:
            for j in i:
                if j in f:
                    f[j] += 1
                else:
                    f[j] = 1
        print(f)
        for i in range(1, r):
            if i not in f:
                miss = i
            elif f[i] == 2:
                rep = i
        return [rep, miss]


s = Solution()
print(s.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
