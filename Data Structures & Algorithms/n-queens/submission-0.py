class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
#        visited = [[False for _ in range(n)] for _ in range(n)]
        board = [ ["." for _ in range(n)] for _ in range(n)]
        used_row = set()
        used_col = set()
        used_r_plus_c = set()
        used_r_minus_c = set()
        result = []
#        result = [[None for _ in range(n)] for _ in range(n)]
#        print(board)

        def dfs(row):

            if row == n:
                result.append( ["".join(row) for row in board] )
                print(result)
                return

            for col in range(n):
                if (not (row) in used_row and not col in used_col 
                    and not (row) + col in used_r_plus_c 
                    and not (row) - col in used_r_minus_c
                    ):

                    used_row.add(row)
                    used_col.add(col)
                    used_r_plus_c.add(row + col)
                    used_r_minus_c.add(row - col)
                    board[row][col] = 'Q'
                    dfs(row + 1)
                    board[row][col] = '.'
                    used_row.remove(row)
                    used_col.remove(col)
                    used_r_plus_c.remove(row + col)
                    used_r_minus_c.remove(row - col)


        dfs(0)
        print(result)

        return result