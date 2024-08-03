class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def map_number(num: int) -> int:
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_str)

        l = [(map_number(num), i) for i, num in enumerate(nums)]
        l.sort()
        op = [nums[i[1]] for i in l]
        return op


sol = Solution()
print(
    sol.sortJumbled(
        [5, 6, 8, 7, 4, 0, 3, 1, 9, 2], [7686, 97012948, 84234023, 2212638, 99]
    )
)
