class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()

        unique_q = list( {q for q in queries} )
        unique_q.sort()

        minheap= []

        # q0 = queries[0]
        # for i in range(len(intervals)):
        #     if intervals[i][0] <= q0 <= intervals[i][1]:
        #         length = intervals[i][1] - intervals[i][0] + 1
        #         heapq.heappush(minheap, (length, intervals[i][1]) )
        #     if q0 < intervals[i][0]:
        #         break
        # print(i, q0, intervals[i])

        # print(minheap, i)

#        print(intervals)
#        print(unique_q)
        res = {}

        i = 0
        for iq in range(0, len(unique_q)):
            q = unique_q[iq]
#            print(f'q = {q}, i = {i}')

            while i < len(intervals) and intervals[i][0] <= q:
                length = intervals[i][1] - intervals[i][0] + 1
#                print(f'adding {intervals[i]}')
                heapq.heappush(minheap, (length, intervals[i][1]) )
                i += 1

#            print(f'minheap = {minheap}')

            minlen = -1
            while minheap and minheap[0][1] < q:
                minlen, end = heapq.heappop(minheap)
            if minheap:
#                print(f'q = {q}, res = {minheap[0][0]}')
                res[q] = minheap[0][0]

        fr = []
        for q in queries:
            if q in res:
                fr.append(res[q])
            else:
                fr.append(-1)

        return fr

