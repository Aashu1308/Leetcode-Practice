from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        sums = []
        for i in range(n):
            for j in range(i, n):
                sums.append(prefix[j + 1] - prefix[i])
        sums.sort()
        MOD = 10**9 + 7
        return sum(sums[i] for i in range(left - 1, right)) % MOD


sol = Solution()
print(sol.rangeSum([1, 2, 3, 4], 4, 1, 10))
