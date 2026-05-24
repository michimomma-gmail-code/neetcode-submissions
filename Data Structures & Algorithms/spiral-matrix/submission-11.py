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

        def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            m, n = len(matrix), len(matrix[0])
            state = 0
            visited = set()

            r, c = 0
            res = []

            direction = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

            for i in range( m * n ):

                res.append( matrix[r][c] )
                visited( (r, c) )
                for i in range(4):
                    if state == i:
                        next_r, next_c = r + direction[state][0], c + direction[state][1]
                        break
                
                if next_r < 0 or next_r >= m or next_c < 0 or next_c >= n or (next_r, next_c) in visited:
                    state += 1
                    state = state % 4
                    next_r, next_c = r + direction[state][0], c + direction[state][1]

            return res
            
                

            




        