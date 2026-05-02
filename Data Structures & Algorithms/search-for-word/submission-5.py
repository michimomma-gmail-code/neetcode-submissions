class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        max_i = len(board)
        max_j = len(board[0])

        visited = [ [False for _ in range(max_j)] for _ in range(max_i) ]

        def dfs(i, j, index):
            if index == len(word):
                return True
            
            if (i >= max_i or j >= max_j or i < 0 or j < 0 
            or visited[i][j] or board[i][j] != word[index]):
                return False

            visited[i][j] = True
            res = (dfs(i + 1, j, index + 1) or dfs(i - 1, j, index + 1) 
                or dfs(i, j - 1, index + 1) or dfs(i, j + 1, index + 1))
            visited[i][j] = False

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False