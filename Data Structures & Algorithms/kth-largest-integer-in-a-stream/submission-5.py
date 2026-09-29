class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush( self.minheap, val )
        else:
            if self.minheap[0] < val:
                heapq.heappushpop(self.minheap, val)

        return self.minheap[0]
