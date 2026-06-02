class StockSpanner:
    # monotinic decrease?
    # (100, 1) -> (80, 1) -> (60, 1) -> (70, 1) 
    # (100, 1) -> (80, 1) -> (70, 2) 
    # (100, 1) -> (80, 1) -> (70, 2) -> (60, 1) 
    # (100, 1) -> (80, 1) -> (70, 2) -> (60, 1) -> (75, 1)
    # (100, 1) -> (80, 1) -> (75, 4)
    # (100, 1) -> (80, 1) -> (75, 4) -> (85, 1)
    # (100, 1) -> (85, 6)
    # (100, 1) -> (85, 6) -> (85, 1)
    # (100, 1) -> (85, 7) 

    #
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # if len(self.stack) == 0:
        #     self.stack.append( (price, 1) )
        #     return 1
        
        # if self.stack[-1][0] > price:
        #     self.stack.append( (price, 1) )
        #     return 1
        # else:
        counts = 1
        while self.stack and self.stack[-1][0] <= price:
            p, c = self.stack.pop()
            counts += c
        self.stack.append( (price, counts) )
    
        return counts
    




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)