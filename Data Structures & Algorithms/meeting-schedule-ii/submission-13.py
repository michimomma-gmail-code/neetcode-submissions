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

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key = lambda i: i.start)
        # cur_time = intervals[i].start
        # push this inteval to the queue (endtime, index)
        # if cur_time == queue[0][0] (end time of 1st in the queue)
        # then pop
        # len of queue is the rooms needed
        #
        cur = intervals[0]
        t = cur.start
        minheap = []
        heapq.heappush(minheap,  (cur.end, 0) )
        n = len(intervals)
        max_num_rooms = 1
        for i in range(1, n):
            cur = intervals[i]
            t = cur.start
            if minheap[0][0] <= t:
                print(f't = {t}, pop {minheap[0]}')
                heapq.heappop(minheap)
            heapq.heappush(minheap, (cur.end, i) )
            print(t, minheap)
            max_num_rooms = max(max_num_rooms, len(minheap))
        
        return max_num_rooms

