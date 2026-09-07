class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])

        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, prev, reachable):
            if not (0 <= i < m) or not (0 <= j < n):
                return

            if heights[i][j] < prev:
                return

            if (i, j) in reachable:
                return

            reachable.add( (i, j) )

            for di, dj in delta:
                ni, nj = i + di, j + dj
                dfs(ni, nj, heights[i][j], reachable)

            return 

        pacific_reachable = set()
        for i in range(m):
            dfs(i, 0, -1, pacific_reachable)
        for j in range(n):
            dfs(0, j, -1, pacific_reachable)

        atlantic_reachable = set()
        for i in range(m):
            dfs(i, n - 1, -1, atlantic_reachable)
        for j in range(n):
            dfs(m - 1, j, -1, atlantic_reachable)

        res = atlantic_reachable & pacific_reachable
        return [ [i, j]  for (i, j) in res  ]
    
