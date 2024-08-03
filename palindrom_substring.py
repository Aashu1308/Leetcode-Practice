class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandCenter(l: int, r: int) -> (int, int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start = 0
        end = 0
        for i in range(len(s)):
            l1, r1 = expandCenter(i, i)
            l2, r2 = expandCenter(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start : end + 1]


sol = Solution()
print(sol.longestPalindrome("cbbd"))  # bb
