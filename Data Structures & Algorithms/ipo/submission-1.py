class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # maximize capital
        #
        # profit[i] -> capital[i + 1] -> profit[i + 1]
        #
        # k = 3, w = 0, 
        # profit  = [1,4,2,3]
        # capital = [0,3,1,1]
        # w = 0 -> profit[0] = 1 -> profit[3] = 3 -> profit[1] = 4
        #  capital 0                 0 + 1           0 + 1 + 3      0 + 1 + 3 + 4 
        #
        # k = 4, w = 2
        # profit  = [2,3,1,5,3]
        # capital = [4,4,2,3,3]
        # w = 2 -> profit[2] = 1 -> profit[3] = 5 -> profit[4] = 3 -> profit[1] = 3
        #          2 + 1            2 + 1 + 5        2 + 1 + 5 + 3.   2 + 1 + 5 + 3 + 3 = 14

        # max profit s.t. capital <= cur_cap
        #
        # sort initial capital. 
        # profit  = [1,2,3,4]
        # capital = [0,1,1,3]
        # cur_cap = w + sum profit
        # max_heap to identify max profit, given capital <= cur_capital 
        # udate max_heap to include capital <= cur_capital
        #

        # shortcut check
        min_cap = min(capital)
        if min_cap > w:
            return w

        n = len(profits)
        index_sorted = [i for i in range(n)]
        index_sorted.sort(key = lambda i: capital[i])
        profits_sorted = [profits[index_sorted[i]] for i in range(n)]
        capital_sorted = [capital[index_sorted[i]] for i in range(n)]

        print(capital_sorted)
#        profit_sorted = 
        max_heap = []
        cur_cap = w
        
        i = 0
        num_proj = 0
        while i < n or num_proj <= k:
            while i < n and capital_sorted[i] <= cur_cap:
                heapq.heappush(max_heap, (-profits_sorted[i], capital_sorted[i]))
                i += 1
            
            neg_pf, cap = heapq.heappop(max_heap)
            cur_cap += -neg_pf

            num_proj += 1
            if num_proj == k:
                return cur_cap

#        print(f'left over = {max_heap}')
        return cur_cap
