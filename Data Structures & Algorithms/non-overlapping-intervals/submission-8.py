class Solution:
    def eraseOverlapIntervals0(self, intervals: List[List[int]]) -> int:
        
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

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        n = len(intervals)
        dp = [1] * (n)
        dp[0] = 1

        for i in range(1, n):
            current = intervals[i]

            for j in range(i):
                prev = intervals[j]
                if prev[1] <= current[0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        print(dp)
        return n - dp[-1]

