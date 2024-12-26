class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]

        #         if profit > 0:
        #             max_profit = max(max_profit, profit)

        # return max_profit if max_profit > float(-inf) else 0
                
        l = 0
        r = 1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r +=1

        return max_profit if max_profit > float('-inf') else 0
        
    # Time Complexity: O(n)
    # Space Complexity: O(1)