class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        op = 0
        sub = False
        for i in range(n):
            cur = s[i]
            if not sub:
                try:
                    nxt = s[i + 1]
                    if val[nxt] > val[cur]:
                        op += val[nxt] - val[cur]
                        sub = True
                        # print("Value added: ", val[nxt] - val[cur])
                    else:
                        op += val[cur]
                    #     print("Value added: ", val[cur])
                    # print("Sub status: ", sub)
                except IndexError:
                    op += val[cur]
                    # print("Value added: ", val[cur])
            else:
                sub = False
        return op


sol = Solution()
print(sol.romanToInt("MCMXCIV"))  # 1994
