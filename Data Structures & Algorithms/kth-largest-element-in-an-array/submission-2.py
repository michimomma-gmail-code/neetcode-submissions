class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap 
        # push 1st k-th elems
        # for k+1 and beyond
        # if it is larger than minheap[0]
        #   pushpop
        
        minheap = []

        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            else:

                if minheap[0] < num:
                    heapq.heappushpop(minheap, num)

        
        return minheap[0]



