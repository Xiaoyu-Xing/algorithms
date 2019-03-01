class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, profit = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit


# More advance method: Kadane's Algorithm
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
# https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_local, max_global = 0, 0
        for i in range(1, len(prices)):
            max_local = max(0, max_local + prices[i] - prices[i - 1])
            max_global = max(max_global, max_local)
        return max_global
