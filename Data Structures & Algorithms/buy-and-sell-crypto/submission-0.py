class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for currentPrice in prices:
            if (currentPrice < minPrice):
                minPrice = currentPrice
            if (currentPrice - minPrice > maxProfit):
                maxProfit = currentPrice - minPrice
        return maxProfit