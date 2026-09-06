class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, idx):
            if not (0 <= i < m) or not (0 <= j < n):
                return False

#            print("trying ", board[i][j], board)


            if board[i][j] == "":
                return False

            if word[idx] != board[i][j]:
                return False

            if idx == len(word) - 1:
                return True

#            print("match: ", word[idx])

            temp = board[i][j]
            board[i][j] = ""

            for di, dj in d:
                if dfs(i + di, j + dj, idx + 1):
                    return True

            board[i][j] = temp

            
            return False

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
