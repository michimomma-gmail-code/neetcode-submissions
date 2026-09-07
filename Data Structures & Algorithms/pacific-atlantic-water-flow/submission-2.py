class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])

        pacific_reachable = set()
        for i in range(m):
            pacific_reachable.add( (i, 0) )
        for j in range(n):
            pacific_reachable.add( (0, j) )

        atlantic_reachable = set()
        for i in range(m):
            atlantic_reachable.add( (i, n - 1) )
        for j in range(n):
            atlantic_reachable.add( (m - 1, j) )

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
                temp = dfs(ni, nj, heights[i][j], reachable)
                if temp:
                    reachable.update(temp)

            return reachable

        new_reachable = set()
        for i, j in pacific_reachable:
            temp = dfs(i, j, -1, new_reachable)
            if temp:
                new_reachable.update(temp)
               
        pacific_reachable.update(new_reachable)

#        print(sorted(pacific_reachable))
        
        new_reachable = set()
        for i, j in atlantic_reachable:
            temp = dfs(i, j, -1, new_reachable)
            if temp:
                new_reachable.update(temp)
               
        atlantic_reachable.update(new_reachable)

#        print(sorted(atlantic_reachable))
        res = atlantic_reachable & pacific_reachable
        return [ [i, j]  for (i, j) in res  ]
    
