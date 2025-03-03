from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        a = []
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i][0] < nums2[j][0]:
                a.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                a.append(nums2[j])
                j += 1
            else:
                a.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
        if i < n1:
            while i < n1:
                a.append(nums1[i])
                i += 1
        if j < n2:
            while j < n2:
                a.append(nums2[j])
                j += 1
        return a
