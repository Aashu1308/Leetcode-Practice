from typing import List
from itertools import combinations


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        d = {}
        for i in range(n):
            for j in range(i + 1, n):
                k = nums[i] * nums[j]
                if k not in d:
                    d[k] = 0
                d[k] += 1
        # for key in d:
        #     if len(d[key]) >= 2:  # Check if there are at least 2 pairs
        #         # Generate all possible combinations of pairs
        #         for _ in combinations(d[key], 2):
        #             # # Pairs are already tuples, no need for additional unpacking
        #             # print(
        #             #     f"Pairs with product {key}: {pair1} and {pair2} and {pair1[::-1]} and {pair2[::-1]}"
        #             # )
        #             count += 4 * 2
        for freq in d.values():
            if freq >= 2:
                # nC2 * 8 : Choose 2 pairs from freq pairs * 8 permutations
                count += (freq * (freq - 1) // 2) * 8
        return count


s = Solution()
print(s.tupleSameProduct([2, 3, 4, 6]))
