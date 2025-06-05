class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        min_price = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, prices[i])

        return max_profit if max_profit > 0 else 0

    # Time Complexity: O(n)
    # Space Complexity: O(1)
