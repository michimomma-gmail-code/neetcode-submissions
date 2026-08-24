class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        prof = 0
        for i in range(1, len(prices)):
            prof = max(prof, prices[i] - minval)
            minval = min(minval, prices[i])
        
        return prof
