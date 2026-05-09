class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []        
        nrow, ncol = len(heights), len(heights[0])

        delta = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable, prev_height):

            if (not (0 <= r < nrow and 0<= c < ncol) 
                or heights[r][c] < prev_height
                or (r,c) in reachable
                ):
                return

            reachable.add( (r, c) )

            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, reachable, heights[r][c])

        
        for c in range(ncol):
            dfs(0, c, pacific_reachable, heights[0][c]) 
        for r in range(nrow):
            dfs(r, 0, pacific_reachable, heights[r][0]) 

        for c in range(ncol):
            dfs(nrow - 1, c, atlantic_reachable, heights[nrow - 1][c]) 
        for r in range(nrow):
            dfs(r, ncol - 1, atlantic_reachable, heights[r][ncol - 1]) 

        temp = atlantic_reachable.intersection(pacific_reachable)
        res = []
        for r, c in temp:
            res.append([r,c])
        
        return res

        