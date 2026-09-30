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

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = [ [] for _ in range( len(nums) + 1 ) ]

        for c in count:
            bucket[count[c]].append(c)

        cnt = 0
        res = []
        for i in range(len(bucket) -1, -1, -1):
            if bucket[i]:
                for _n in bucket[i]:
                    cnt += 1
                    res.append(_n)
                    if len(res) == k:
                        return res
                
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
#        print(freq)

        bucket = [ [] for _ in range(len(nums) + 1)] 

#        print(bucket)

        for n, c in freq.items():
            bucket[c].append(n)

#        print(bucket)

        out = []
        for i in range(len(bucket) -1, -1, -1):
            if bucket[i]:
                for j in range(len(bucket[i])):
                        out.append(bucket[i][j])
                        if len(out) == k:
                            return out












































