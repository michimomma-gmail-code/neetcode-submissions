class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        zerorow = [False] * m
        zerocol = [False] * n

        for r in range(m):
            for c  in range(n):
                if matrix[r][c] == 0:
                    zerorow[r] = zerocol[c] = True

        for r in range(m):
            if zerorow[r]:
                matrix[r] = [0] * n
        
        for c in range(n):
            if zerocol[c]:
                for r in range(m):
                    matrix[r][c] = 0

