class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        for i in range(1, len(prices), 1):
            profit = prices[i] - minBuy
            if profit > maxProfit:
                maxProfit = profit
            
            if prices[i] < minBuy:
                minBuy = prices[i]
        
        return maxProfit