from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            if len(digits) == 1:
                return [1, 0]
            else:
                x = -1
                while abs(x) <= len(digits) and digits[x] == 9:
                    digits[x] = 0
                    x -= 1
                if abs(x) > len(digits):
                    digits.insert(0, 1)
                else:
                    digits[x] += 1
                return digits
