class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # math
        if len(prices) == 1:
            return 0

        buy_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                profit = max(profit, prices[i] - buy_price)

        return profit
