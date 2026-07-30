class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nrow = len(matrix)
        ncol = len(matrix[0])

        if nrow == ncol:
            for r in range(nrow):
                for c in range(r + 1, ncol):
                    matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]
            
            return matrix

        tr = [[0] * nrow for _ in range(ncol)]

        for r in range(nrow):
            for c in range(ncol):
                tr[c][r] = matrix[r][c]

        return tr