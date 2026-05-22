"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = [inv.start for inv in intervals]
        ends = [inv.end for inv in intervals]

        starts.sort()
        ends.sort()

        i_s = 0
        i_e = 0
        num_rooms = 0
        max_num_rooms = 0
        while i_s < len(starts) and i_e < len(ends):
            if starts[i_s] < ends[i_e]:
                num_rooms += 1
                i_s += 1
            else:
                num_rooms -= 1
                i_e += 1
            max_num_rooms = max(max_num_rooms, num_rooms)

        return max_num_rooms