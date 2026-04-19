class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row_l, row_u = 0, m - 1
        col_l, col_u = 0, n - 1

        row = -1
        while row_l <= row_u:
            mid = row_u + (row_l - row_u) // 2
#            print(f'mid = {mid}')
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target > matrix[mid][-1]:
                row_l = mid + 1
            else:
                row_u = mid - 1
        if row == -1:
            return False

#        print(f'row = {row}')
        data = matrix[row]

        while col_l <= col_u:
            mid = col_u + (col_l - col_u) // 2
            if data[mid] == target:
                return True
            elif target > data[mid]:
                col_l = mid + 1
            else:
                col_u = mid -1

        return False