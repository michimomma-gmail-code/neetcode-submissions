class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        visited = set()
        res = []
        m = len(matrix)
        n = len(matrix[0])

        def dfs(r, c):
            if 0 > r or r >= m or 0 > c or c >= n:
                return False

#            print(f'doing ({r}, {c})')
#            print(f'visited = {visited}, matrix = {matrix[r][c]}')

            if (r, c) in visited:
                return False

            visited.add( (r, c) )
            res.append( matrix[r][c] )
            self.r = r
            self.c = c

            if len(visited) == m * n:
                return True

            while True:
                if self.state % 4 == 0:
                    if not dfs(self.r, self.c + 1):
                        self.state += 1
#                        print(f'state increment = {self.state}')
                    else:
                        return True
                if self.state %4 == 1:
#                    print(f'doing state {self.state}')
                    if not dfs(self.r + 1, self.c):
                        self.state += 1
                    else:
                        return True
                if self.state %4 == 2:
                    if not dfs(self.r, self.c - 1):
                        self.state += 1
                    else:
                        return True
                if self.state %4 == 3:
                    if not dfs(self.r - 1, self.c):
                        self.state += 1
                    else:
                        return True
        
        self.state = 0
        dfs(0, 0)
        return res

        