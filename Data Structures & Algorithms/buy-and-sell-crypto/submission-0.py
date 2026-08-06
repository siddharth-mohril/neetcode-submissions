class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0  # Buy day
        R = 1  # Sell day
        max_profit = 0
        
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
            else:
                # We found a new lower buy price! Jump L to R
                L = R
                
            # Always advance Sell day
            R += 1
            
        return max_profit