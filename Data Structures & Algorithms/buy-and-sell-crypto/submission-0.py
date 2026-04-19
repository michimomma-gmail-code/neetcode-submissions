class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue = 100

        maxvalue = -1

        lenp = len(prices)
        maxvalues = [0] * (lenp)
        
        #
        # prices =      [2 3 1]
        # maxvalues = [3 3 1]

        for i in range(lenp):
            index = lenp - i - 1
            if prices[index] > maxvalue:
                maxvalue = prices[index]
            maxvalues[index] = maxvalue

        #print(maxvalues)

        maxgain = 0
        for i in range(lenp - 1):
            p = prices[i]
#            print(p,i)
            if p < minvalue:
                minvalue = p
            gain = maxvalues[i+1] - minvalue 
            if gain > maxgain:
                maxgain = gain

        return maxgain
        