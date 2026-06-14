class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # adj
        nrow, ncol = len(grid), len(grid[0])

        adj = defaultdict(dict)
        
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    num_nei = 0
                    for dr, dc in delta:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < nrow and 0 <= new_c < ncol and grid[new_r][new_c] == 1:
                            num_nei += 1
                    res += 4 - num_nei
        return res
