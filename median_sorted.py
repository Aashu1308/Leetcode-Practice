from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        n = len(l)
        if not n % 2:
            m = n // 2
            k = m - 1
            median = (l[m] + l[k]) / 2
        else:
            m = n // 2
            median = l[m]
        return median


s = Solution()
n = [1, 2]
m = [3]
print(s.findMedianSortedArrays(n, m))  # Output: 2.0
