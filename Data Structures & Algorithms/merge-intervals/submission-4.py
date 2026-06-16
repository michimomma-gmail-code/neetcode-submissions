class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = intervals.copy()
        intervals.sort()

        print(intervals)

        n = len(intervals)
        i = 0
        old = intervals[0]
        res = []
        while i < n - 1:
            new = intervals[i + 1]
            if old[1] >= new[0]: #merge
                old = [ old[0], max(old[1], new[1]) ]
            else:
                res.append(old)
                old = new
            i += 1

        res.append(old)        
        return res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#        intervals = intervals.copy()
        intervals.sort()

        n = len(intervals)
        res = [intervals[0]]

        for i in range(1, n):
            last_added = res[-1]
            current = intervals[i]

            if last_added[1] >= current[0]:
                last_added[1] = max(last_added[1], current[1])
            else:
                res.append(current)
        
        return res


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [1, 3], [1, 5], [6, 7]
        # track active intervals, merge if there is overlap
        #
        # 1
        # 1         6
        #    3  5    7
        #
        # (1, 1, 6)
        # (3, 5, 7)
        # [1, 1,  3,  5, 6,  7]
        # [1, 1, -1, -5, 1, -1]

        timeline = []
        direction = []

        for st, ed in intervals:
            timeline.append(st)
            timeline.append(ed)
            direction.append(False)
            direction.append(True)

        time_direc = sorted(zip(timeline,direction))
        print(time_direc)

        stack = [time_direc[0]]

        start = stack[-1][0]
        end = start
        res = []
        for i in range(1, len(time_direc)):
            if not time_direc[i][1]:
                stack.append(time_direc[i])
                start = min(start, time_direc[i][0])
            else:
                temp = stack.pop()
                end = max(end, time_direc[i][0])
            if not stack:
                res.append( [start, end] )
                start = time_direc[-1][0]
                end = 0
        return res






























