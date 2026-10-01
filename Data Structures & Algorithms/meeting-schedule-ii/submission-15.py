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

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time_stamp = []
    
        for inv in intervals:
            s = inv.start
            e = inv.end
            time_stamp.append( (s, 1) )
            time_stamp.append( (e, -1) )


#        time_stamp.sort()
#        print(time_stamp)
        time_stamp.sort(key = lambda x: (x[0], x[1]))
#        print(time_stamp)
        max_score = -float('inf')
        cum_score = 0
        for time, score in time_stamp:
            cum_score += score
            max_score = max(max_score, cum_score)
    
        return max_score if max_score > -float('inf') else 0