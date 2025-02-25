"""
https://neetcode.io/problems/buy-and-sell-crypto
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit: int = 0
        buy: int = prices[0]

        for price in prices[1:]:
            profit = max(profit, price - buy)
            buy = min(buy, price)

        return profit


if __name__ == "__main__":
    solution: Solution = Solution()
    print(solution.maxProfit([10, 1, 5, 6, 7, 1]))
    print(solution.maxProfit([10, 8, 7, 5, 2]))
