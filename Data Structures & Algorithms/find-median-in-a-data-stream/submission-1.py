class MedianFinder:

    def __init__(self):
        self.lowerhalf = [] # [1 2 (3)] -- maxheap
        self.higherhalf = [] # [4 5] -- minheap

    def addNum(self, num: int) -> None:

        heapq.heappush(self.lowerhalf, -num)
        maxelem = -heapq.heappop(self.lowerhalf)
        heapq.heappush(self.higherhalf, maxelem)

        if len(self.higherhalf) > len(self.lowerhalf):
            minelem = heapq.heappop(self.higherhalf)
            heapq.heappush(self.lowerhalf, -minelem)
        
    def findMedian(self) -> float:
        if len(self.lowerhalf) == len(self.higherhalf):
            return (-self.lowerhalf[0] + self.higherhalf[0])/ 2
        else:
            return -self.lowerhalf[0]
        