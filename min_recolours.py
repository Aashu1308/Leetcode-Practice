class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minw = 0
        cc = 0
        for i in blocks[:k]:
            if i == 'W':
                cc += 1
        minw = cc
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                cc -= 1
            if blocks[i] == 'W':
                cc += 1
            minw = min(cc, minw)
        return minw
