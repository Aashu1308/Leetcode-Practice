from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) > 1:
        #     m = min(strs, key=len)
        #     if m:
        #         ss = m[0]
        #     else:
        #         ss = ""
        #     matched = False
        #     f = True
        #     for i in range(len(m)):
        #         if f and i != 0:
        #             ss += m[i]
        #         for j in range(len(strs)):
        #             if strs[j][i] == ss[i]:
        #                 matched = True
        #                 pass
        #             else:
        #                 f = False
        #                 matched = False
        #                 break
        #         if not f:
        #             break
        #         print(ss, matched)
        #     if ss:
        #         if matched:
        #             return ss
        #         else:
        #             return ss[:-1]
        #     else:
        #         return ss[:-1]
        # else:
        #     return strs[0]
        if len(strs) == 1:
            return strs[0]
        m = min(strs, key=len)
        if not m:
            return ""
        for i in range(len(m)):
            char = m[i]
            if not all(s[i] == char for s in strs):
                return m[:i]
        return m


sol = Solution()
strs = ["flower", "flow"]
print(sol.longestCommonPrefix(strs))
