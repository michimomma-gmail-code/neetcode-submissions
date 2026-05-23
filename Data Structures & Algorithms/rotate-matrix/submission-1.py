class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # [ [1 2], [3 4] ] -> [ [1 3] [2 4] ] -> [ [3 1] [4 2] ]
        # 
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
                matrix[i].reverse()
        #n =2
        # matrix[0][0] = matrix[0][1 - 0] = matrix[0][1]
        # matrix[0][1] = matrix[0][1 - 1] = matrix[0][0]
        