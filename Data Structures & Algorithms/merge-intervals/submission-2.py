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

