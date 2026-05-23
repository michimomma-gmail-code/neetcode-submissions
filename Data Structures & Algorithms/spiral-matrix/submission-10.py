class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        visited = set()
        res = []
        m = len(matrix)
        n = len(matrix[0])

        direction = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

        def dfs(r, c):
            if 0 > r or r >= m or 0 > c or c >= n:
                return False

            if (r, c) in visited:
                return False

            visited.add( (r, c) )
            res.append( matrix[r][c] )
            self.r = r
            self.c = c

            if len(visited) == m * n:
                return True

            while True:
#                for dr, dc in direction:
                for i in range(4):
                    if self.state == i:
                        dr, dc = direction[i]
                        if not dfs(self.r + dr, self.c + dc):
                            self.state += 1
                            self.state = self.state % 4
                        else:
                            return True
        self.state = 0
        dfs(0, 0)
        return res

        