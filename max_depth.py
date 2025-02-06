class Solution:
    def maxDepth(self, s: str) -> int:
        slen = 0
        mx = 0
        for i in s:
            if i == '(':
                slen += 1
                mx = max(slen, mx)
            elif i == ')':
                slen -= 1
        mx = max(slen, mx)
        return mx
