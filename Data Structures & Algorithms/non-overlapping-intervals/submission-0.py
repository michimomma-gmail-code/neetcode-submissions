class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        print(intervals)
        n = len(intervals)
        res = [intervals[0]]
        delete = 0
        for i in range(1, n):
            prev = res[-1]
            current = intervals[i]

            if prev[1] > current[0]:
                delete += 1
                if prev[1] > current[1]:
                    res.pop()
                    res.append(current)
            else:
                res.append(current)

        return delete