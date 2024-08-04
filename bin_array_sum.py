from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        hashmap = {0: 1}
        current = 0
        for i in nums:
            current += i
            if current - goal in hashmap:
                count += hashmap[current - goal]
            if current in hashmap:
                hashmap[current] += 1
            else:
                hashmap[current] = 1
        return count


sol = Solution()
print(sol.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
