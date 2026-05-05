class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        #visited = [[False for _ in range(n)] for _ in range(n)]
        c_sel = set()
        rc_sel = set()
        nrc_sel = set()
        results = []
        def dfs(r):
            if r == n:
                results.append( [ "".join(row) for row in board ] )
                return

            for c in range(n):
                
                rc = r + c
                nrc = r - c

                if (not c in c_sel and not rc in rc_sel and not nrc in nrc_sel):

                    c_sel.add(c)
                    rc_sel.add(rc)
                    nrc_sel.add(nrc)

                    board[r][c] = "Q"
                    dfs(r + 1)

                    c_sel.remove(c)
                    rc_sel.remove(rc)
                    nrc_sel.remove(nrc)
                    board[r][c] = "."

        dfs(0)
        return results
