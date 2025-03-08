class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        mx = 1
        cc = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                cc += 1
                mx = max(mx, cc)
            else:
                cc = 1
            print(mx, cc)
        return max(mx, cc)


s = Solution()
print(f"op is {s.maxPower('abbcccddddeeeeedcba')}")
