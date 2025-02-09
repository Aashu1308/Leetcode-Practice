class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        v = 0
        while l <= r:
            h = min(height[l], height[r])
            v = max(v, h * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return v
