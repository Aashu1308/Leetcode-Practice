class Solution:
    def intToRoman(self, num: int) -> str:
        rom_dict = {
            0: [1000, 'M'],
            1: [900, 'CM'],
            2: [500, 'D'],
            3: [400, 'CD'],
            4: [100, 'C'],
            5: [90, 'XC'],
            6: [50, 'L'],
            7: [40, 'XL'],
            8: [10, 'X'],
            9: [9, 'IX'],
            10: [5, 'V'],
            11: [4, 'IV'],
            12: [1, 'I'],
        }
        sol = ""
        i = 0
        while num > 0:
            count = num // rom_dict[i][0]
            num %= rom_dict[i][0]
            sol += rom_dict[i][1] * count
            i += 1
        return sol


sol = Solution()
print(sol.intToRoman(3749))
