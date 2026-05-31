class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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

        print(minprices)
        print(maxprices)

        return maxprof