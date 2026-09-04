class MedianFinder:

    def __init__(self):
        self.lowerhalf = [] #max heap
        self.upperhalf = [] #min heap
        self.count = 0

    def addNum(self, num: int) -> None:

        prev_lh = None
        prev_uh = None
        if len(self.lowerhalf) > 0:
            prev_lh = self.lowerhalf[0]
        if len(self.upperhalf) > 0:        
            prev_uh = self.upperhalf[0]

        heapq.heappush(self.lowerhalf, -num)
        heapq.heappush(self.upperhalf, num)

        if prev_lh:
            heapq.heappush(self.lowerhalf, -prev_uh)
        if prev_uh:
            heapq.heappush(self.upperhalf, -prev_lh)

        self.count += 1
        if self.count % 2 == 0: # even
            h = self.count / 2
        else:
            h = self.count // 2 + 1

#        print(f'h = {h}')
        while len(self.lowerhalf) > h:
            heapq.heappop(self.lowerhalf)
#            print(f'remove {heapq.heappop(self.lowerhalf)}')
        while len(self.upperhalf) > h:
            heapq.heappop(self.upperhalf)


    def findMedian(self) -> float:
#        print(f'lh = {-self.lowerhalf[0]}, hh = {self.upperhalf[0]}')
        return (-self.lowerhalf[0] + self.upperhalf[0]) / 2







    def __init__(self):
        self.n = 0
        self.max_heap = [] # for top n//2
        self.min_heap = [] # for low n//2

    def addNum(self, num: int) -> None:
        self.n += 1

        capacity = (self.n + 1) // 2
        # n = 1 -> [1] [1]
        # n = 2 -> [1] [2]
        # n = 3 -> [1 <3>] [<2> 3] : [1 2] [2 3]
        # n = 4 -> [1 <3>] [<3> 4] : [1 2] [<3> 4]
        # n = 5 -> [1 2 3] [3 4 5]
        # n = 6 -> [1 2 3] [4 5 6]
        # n = 7 -> [1 2 3 4 = min(7,4)] [4 5 6 7 = max(3, 7)]
        # n = 8 -> [1 2 3 4 min(8,4)] [4 5 6 7 max(4, 8)]

        # top half
        new_val = num
        if self.min_heap:
            new_val = min(new_val, self.min_heap[0]) 
        
        heapq.heappush( self.max_heap,  - new_val)
        # bottom half
        new_val = num
        if self.max_heap:
            new_val = max(new_val, - self.max_heap[0]) 


        if self.max_heap:
            heapq.heappush( self.min_heap, max(num, -self.max_heap[0]) )
        else:
            heapq.heappush( self.min_heap, num )

        while len(self.max_heap) > capacity:
            heapq.heappop(self.max_heap)

        while len(self.min_heap) > capacity:
            heapq.heappop(self.min_heap)

    def findMedian(self) -> float:

        if self.n % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return self.min_heap[0]


































