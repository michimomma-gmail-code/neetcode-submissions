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

        print(f'h = {h}')
        while len(self.lowerhalf) > h:

            print(f'remove {heapq.heappop(self.lowerhalf)}')
        while len(self.upperhalf) > h:
            heapq.heappop(self.upperhalf)


    def findMedian(self) -> float:
        print(f'lh = {-self.lowerhalf[0]}, hh = {self.upperhalf[0]}')
        return (-self.lowerhalf[0] + self.upperhalf[0]) / 2
