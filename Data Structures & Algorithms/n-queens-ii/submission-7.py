class Solution:
    def totalNQueens(self, n: int) -> int:
        
        visited = set()
        cols, row_col, row_m_col = set(), set(), set()


        res = []
        def dfs(r, c):
            if r == n:
                res.append( (r, c) )
                return True

            for c in range(n):

                if (c not in cols and (r+c) not in row_col and (r-c) not in row_m_col):

                    cols.add(c)
                    row_col.add(r + c)
                    row_m_col.add((r - c))

                    dfs(r + 1, c)

                    cols.remove(c)
                    row_col.remove(r + c)
                    row_m_col.remove((r - c))

            return 

        
        print(dfs(0, 0))

        print(res)

        return len(res)