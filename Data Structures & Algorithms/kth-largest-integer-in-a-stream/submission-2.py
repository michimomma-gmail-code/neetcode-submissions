class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap_array = nums
        heapq.heapify(self.heap_array)
        while len(self.heap_array) > self.k:
            heapq.heappop(self.heap_array)

    def add(self, val: int) -> int:
        if len(self.heap_array) < self.k:
            heapq.heappush(self.heap_array, val)
        else:
            # may replace
            minelem = self.heap_array[0]
            if val >= minelem:
                heapq.heapreplace(self.heap_array, val)
#                heapq.heappop(self.heap_array)                
#                heapq.heappush(self.heap_array, val)
        return self.heap_array[0]
