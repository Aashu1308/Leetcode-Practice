class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow_c = 0
        cc = 0
        vows = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(k):
            if s[i] in vows:
                cc += 1
        vow_c = cc
        for i in range(k, len(s)):
            if s[i - k] in vows:
                cc -= 1
            if s[i] in vows:
                cc += 1
            vow_c = max(vow_c, cc)
        return vow_c
