"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        
        if not intervals:
            return True

        prev_end = intervals[0].end
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev_end > curr.start:
                return False
            prev_end = max(prev_end, curr.end)

        return True