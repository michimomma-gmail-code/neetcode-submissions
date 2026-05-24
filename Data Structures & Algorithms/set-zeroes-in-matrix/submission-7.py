class Solution:
    def setZeroes0(self, matrix: List[List[int]]) -> None:
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

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        is_col0_zero = False
        is_row0_zero = False

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0
                    if c == 0:
                        is_col0_zero = True
                    if r == 0:
                        is_row0_zero = True


        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(1, n):
                    matrix[r][c] = 0
        
        print(matrix)

        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(m):
                    matrix[r][c] = 0

        if is_col0_zero:
            for r in range(m):
                matrix[r][0] = 0

        if is_row0_zero:
            matrix[0] = [0] * n
