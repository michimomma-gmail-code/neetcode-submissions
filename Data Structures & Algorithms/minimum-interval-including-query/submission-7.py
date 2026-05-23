class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()

        unique_q = sorted( set(queries) )

        minheap= []
#        print(unique_q)
        res = {}

        i = 0
        for iq in range(0, len(unique_q)):
            q = unique_q[iq]

            while i < len(intervals) and intervals[i][0] <= q:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minheap, (length, intervals[i][1]) )
                i += 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            if minheap:
                res[q] = minheap[0][0]

        # fr = []
        # for q in queries:
        #     if q in res:
        #         fr.append(res[q])
        #     else:
        #         fr.append(-1)

        return [res.get(q, -1) for q in queries]

