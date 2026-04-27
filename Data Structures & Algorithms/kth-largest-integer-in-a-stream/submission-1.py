class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap_array = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
#        print(f'len {len(self.heap_array)}')
        if len(self.heap_array) < self.k:
            heapq.heappush(self.heap_array, val)
        else:
            # may replace
            minelem = self.heap_array[0]
            if val >= minelem:
                heapq.heappop(self.heap_array)                
#                print(f'heappop {self.heap_array}, {heapq.heappop(self.heap_array)}, {self.heap_array}')
                heapq.heappush(self.heap_array, val)
#                print(f'heappush {self.heap_array}')
        return self.heap_array[0]
