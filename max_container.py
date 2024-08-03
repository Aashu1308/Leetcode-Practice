class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            if area > max_area:
                max_area = area
        return max_area


sol = Solution()
print(sol.maxArea([1, 1]))
