class MedianFinder:

    def __init__(self):
        self.lo_heap = [] # max heap
        self.hi_heap = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush( self.lo_heap, - num )
        heapq.heappush( self.hi_heap, - heapq.heappop(self.lo_heap) )

        if len(self.hi_heap) > len(self.lo_heap):
            heapq.heappush( self.lo_heap, - heapq.heappop(self.hi_heap) )
        
    def findMedian(self) -> float:
#        print(self.hi_heap, self.lo_heap, len(self.hi_heap) + len(self.lo_heap))
        if (len(self.hi_heap) + len(self.lo_heap)) % 2 == 0:
            return ( self.hi_heap[0] - self.lo_heap[0] ) / 2.0
        else:
            return - self.lo_heap[0]
