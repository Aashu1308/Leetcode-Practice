from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def generate(l, last, curr):
            if l == 0:
                return [curr]

            result = []
            for char in ['a', 'b', 'c']:
                if char == last:
                    continue

                result.extend(generate(l - 1, char, curr + char))
            return result

        op = []
        for i in ['a', 'b', 'c']:
            op.extend(generate(n - 1, i, i))

        op.sort()  # Sort lexicographically

        if k <= len(op):
            return op[k - 1]
        else:
            return ""


# Test
s = Solution()
o = s.getHappyString(3, 9)
print(o)
