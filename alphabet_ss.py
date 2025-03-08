class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        mx = 1
        cc = 1
        for i in range(len(s) - 1):
            if ord(s[i + 1]) - ord(s[i]) == 1:
                cc += 1
                mx = max(mx, cc)
            else:
                cc = 1
            print(cc, mx)
        mx = max(mx, cc)
        return mx


s = Solution()
print("op is:", s.longestContinuousSubstring("yrpjofyzubfsiypfre"))
