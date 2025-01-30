from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # c = [0] * len(A)
        # for i in range(len(A)):
        #     for j in range(i + 1):
        #         if B[j] in A[: i + 1]:
        #             c[i] += 1
        # return c
        c = [0] * len(A)
        f = [0] * (len(A) + 1)
        common = 0
        for i in range(len(A)):
            f[A[i]] += 1
            if f[A[i]] == 2:
                common += 1
            f[B[i]] += 1
            if f[B[i]] == 2:
                common += 1
            c[i] = common
        return c


sol = Solution()
print(
    sol.findThePrefixCommonArray(
        [2, 3, 1],
        [3, 1, 2],
    )
)
