class NumMatrix:
# 
# prefixsum[row2][col2] - prefixsum[row1 -1][col2] - prefixsum[row2][col1 - 1] + prefixsum[row1][col1]
# 21 - 4 - 9 + 3 = 11
#

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        self.prefixsum = [ [0] * n for _ in range(m) ]

        for r in range(m):
            for c in range(n):
                # prefixsum[r][c] = matrix[r][c] + prefixsum[r - 1][c] + prefixsum[r][c - 1] - prefixsum[r - 1][c - 1]
                self.prefixsum[r][c] = matrix[r][c]
                if r > 0 and c > 0:
                    self.prefixsum[r][c] -= self.prefixsum[r - 1][c - 1]
                if r > 0:
                    self.prefixsum[r][c] += self.prefixsum[r - 1][c]
                if c > 0:
                    self.prefixsum[r][c] += self.prefixsum[r][c - 1]

#        print(self.prefixsum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # prefixsum[row2][col2] 
        res = self.prefixsum[row2][col2] 

        if row1 > 0:
            res -= self.prefixsum[row1 - 1][col2]
        if col1 > 0:
            res -= self.prefixsum[row2][col1 - 1]

        if row1 and col1:
            res += self.prefixsum[row1 - 1][col1 - 1] 

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)