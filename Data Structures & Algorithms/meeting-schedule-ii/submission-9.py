"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0
#        if len(intervals) == 1:
#            return 1

        intervals.sort(key = lambda i: i.start)
        print(intervals)

        minheap = [(intervals[0].end, intervals[0].start)]
        #heapq.heapify(minheap)
        #max_active = 0

        for i in range(1, len(intervals)):
            current = intervals[i]
            if current.start >= minheap[0][0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, (current.end, current.start) )

            #max_active = max(max_active, len(minheap))

        return len(minheap)
