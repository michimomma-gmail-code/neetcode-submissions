class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        prof = 0
        for i in range(1, len(prices)):
            prof = max(prof, prices[i] - minval)
            minval = min(minval, prices[i])
        
        return prof

    def maxProfit(self, prices: List[int]) -> int:
        # state
        # hold: maximum profit you can have if you end the day holding a stock
        # sold: maximum profit you can have if you end the day not holding a stock
        # state tarnsition
        # hold -> hold 
        # hold -> sold
        # sold -> hold
        # sold -> sold
        hold = - float("inf")
        sold = 0
        for p in prices:
            hold = max(hold, -p)
            sold = max(sold, hold + p)

        return sold



    def maxProfit(self, prices: List[int]) -> int:
        #
        # state (end of day)
        # 1. hold (have stock)
        # 2. sold (no stock)
        # transition
        # hold = max( keep hold, sold -> buy)
        # sold = max( sold -> sold, hold -> sell)
        hold = - float("inf")
        sold = 0
        for p in prices:
            hold = max(hold,  -p)
            sold = max(sold, p + hold)
        return sold









































