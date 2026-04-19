class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprof = 0
        for i in range(len(prices)):
            diff = prices[i] - minprice
            if diff > maxprof:
                maxprof = diff
            if prices[i] < minprice:
                minprice = prices[i]
        return maxprof
