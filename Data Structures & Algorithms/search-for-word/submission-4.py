class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False

        max_i = len(board)
        max_j = len(board[0])

        self.visited = [ [False for _ in range(max_j)] for _ in range(max_i) ]

        def dfs(i, j, substring):
            
            if len(substring) > len(word) or i >= max_i or j >= max_j or i < 0 or j < 0:
                return 
            if substring == word:
                self.res = True
                return 

            # right
            delta = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
            for (di, dj) in delta:
                if 0 <= i + di < max_i and 0 <= j + dj < max_j and not self.visited[i + di][j + dj]:
                    self.visited[i + di][j + dj] = True
                    dfs(i + di, j + dj, substring + board[i + di][j + dj])
                    self.visited[i + di][j + dj] = False


        initial = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == initial:
                    self.visited[i][j] = True
                    dfs(i, j, initial)
                    self.visited[i][j] = False
                    if self.res == True:
                        return self.res

        return False