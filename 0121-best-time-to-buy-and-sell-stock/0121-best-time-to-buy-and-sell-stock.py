class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TC: O(n), SC: O(1)
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
