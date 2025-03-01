class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_p(ss: str) -> bool:
            return ss == ss[::-1]

        ss = ""
        c = 0
        for i in range(len(s)):
            ss = s[i]
            if is_p(ss):
                c += 1
            for j in range(i + 1, len(s)):
                ss += s[j]
                if is_p(ss):
                    c += 1
        return c
