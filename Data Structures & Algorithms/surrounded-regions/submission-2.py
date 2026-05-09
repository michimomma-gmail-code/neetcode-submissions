class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        nrow = len(board)
        ncol = len(board[0])

        delta = [ (0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):

            if r < 0 or r >= nrow or c < 0 or c >= ncol:
                return
            if  board[r][c] != "O":
                return

            board[r][c] = "#"

            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for r in range(nrow):
            for c in (0, ncol - 1):
                if board[r][c] == "O":
                    dfs(r, c)

        for r in (0, nrow - 1):
            for c in range(ncol):
                if board[r][c] == "O":
                    dfs(r, c)
#        print(board)
    
        for c in range(ncol):
            for r in range(nrow):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

#        print(board)
        