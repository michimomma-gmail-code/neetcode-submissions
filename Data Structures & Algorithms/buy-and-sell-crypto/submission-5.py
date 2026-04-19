class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue = 100

        lenp = len(prices)
        
        maxgain = 0
        for i in range(lenp):
            p = prices[i]
            if p < minvalue:
                minvalue = p
            gain = p - minvalue 
            if gain > maxgain:
                maxgain = gain

        return maxgain
        