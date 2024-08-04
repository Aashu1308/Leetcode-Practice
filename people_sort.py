from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        people.sort(key=lambda x: x[1], reverse=True)
        return [name for name, _ in people]


sol = Solution()
print(sol.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
