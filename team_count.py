from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)
        for j in range(1, n - 1):
            l_left = g_left = l_right = g_right = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    l_left += 1
                else:
                    g_left += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    l_right += 1
                else:
                    g_right += 1
            count += (l_left * g_right) + (g_left * l_right)
        return count


sol = Solution()
print(sol.numTeams([1, 2, 3, 4]))  # 4
