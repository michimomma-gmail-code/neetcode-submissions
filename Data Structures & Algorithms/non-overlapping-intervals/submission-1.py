class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        print(intervals)
        n = len(intervals)
        num_delete = 0
        res = [intervals[0]]

        for i in range(1, n):
            last_added = res[-1]
            current = intervals[i]
            if last_added[1] > current[0]:
                num_delete += 1
                if last_added[1] > current[1]:
                    res.pop()
                    res.append(current)
            else:
                res.append(current)

        return num_delete
        
                    