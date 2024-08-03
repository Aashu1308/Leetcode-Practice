class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lens = 0
        for i in range(len(s)):
            substr = s[i]
            for j in range(i + 1, len(s)):
                if s[j] in substr:
                    break
                else:
                    substr += s[j]
            if len(substr) > lens:
                lens = len(substr)
        return lens


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
