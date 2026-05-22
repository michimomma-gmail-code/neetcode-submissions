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