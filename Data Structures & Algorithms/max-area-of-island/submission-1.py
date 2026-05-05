class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        nrow = len(grid)
        ncol = len(grid[0])
        directions = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

        print('nrow, ncol = ', nrow, ncol)

        def dfs(r, c):
            result = 0

            if r < 0 or r >= nrow or c < 0 or c >= ncol or grid[r][c] != 1:
                return result

            result += 1
            grid[r][c] = 0

            for dr, dc in directions:
                result += dfs(r + dr, c + dc)

            return result
            
        max_res = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    sizei = dfs(r, c)
#                    print(f'sizei = {sizei}')
                    max_res = max(max_res, sizei)

        return max_res