"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda i: i.start)
        prev = intervals[0]
        n = len(intervals)

        for i in range(1,n):
            current = intervals[i]
            if prev.end > current.start:
                return False
            prev = current
        return True