class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
#        print(count)

        minheap = []
        for num in count:
#            print(num, count[num])
            if len(minheap) < k:
                heapq.heappush(minheap, (count[num], num) )
            else:
                if minheap[0][0] < count[num]:
#                   heapq.heappop(minheap)
                   heapq.heappushpop(minheap, (count[num], num) )
#        print(minheap)

        return [minheap[i][1] for i in range(len(minheap))]