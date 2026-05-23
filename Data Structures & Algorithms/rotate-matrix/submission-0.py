class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # [ [1 2], [3 4] ] -> [ [1 3] [2 4] ] -> [ [3 1] [4 2] ]
        # 
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                a = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = a

        for i in range(n):
            for j in range(n // 2):
                a = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = a

        #n =2
        # matrix[0][0] = matrix[0][1 - 0] = matrix[0][1]
        # matrix[0][1] = matrix[0][1 - 1] = matrix[0][0]
        