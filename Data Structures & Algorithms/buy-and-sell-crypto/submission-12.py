class Solution:
    def maxProfit0(self, prices: List[int]) -> int:
        minprices = []
        minp = prices[0]
        for i in range(len(prices)):
            p = prices[i]
            if p < minp:
                minp = p
            minprices.append(minp)

        maxprices = []
        maxp = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            p = prices[i]
            if p > maxp:
                maxp = p
            maxprices.append(maxp)

        maxprices.reverse()
        
        maxprof = 0
        for i in range(len(prices) - 1):
            prof = maxprices[i + 1] - minprices[i]
            maxprof = max(0, maxprof, prof)

        return maxprof

    def maxProfit1(self, prices: List[int]) -> int:

        # left: track min val
        # right: explore max val

        left, right = 0, 1
        maxP = 0

        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                maxP = max(maxP, prices[right] - prices[left])
            else:
                # prices[left] >= prices[right] -> replace to get lower value (min)
                left = right

        return maxP

    def maxProfit(self, prices: List[int]) -> int:
        # hold. (bought in the past. no sell) 
        # no stock (sell or keep pause. no stock)
        # initial
        hold = -float("infinity")
        nostock = 0
        for i in range(len(prices)):
            nostock = max(nostock, prices[i] + hold)
            hold = max(hold, -prices[i])
        
        return nostock
        