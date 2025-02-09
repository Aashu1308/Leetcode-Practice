from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = float('inf')
        for price in prices:
            if price < min_p:
                min_p = price
            elif price - min_p > profit:
                profit = price - min_p
        return profit
