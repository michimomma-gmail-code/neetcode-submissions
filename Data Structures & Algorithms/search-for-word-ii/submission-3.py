class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()

        for word in words:
            cur = root
            for char in word:    
                if not char in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.word = word

        result = []
        nrows = len(board)
        ncols = len(board[0])

        def dfs(r, c, node):
            if r < 0 or r >= nrows or c < 0 or c >= ncols or board[r][c] not in node.children:
                return

            temp = board[r][c]

            if node.children[temp].word: 
                result.append(node.children[temp].word)
                node.children[temp].word = None

            board[r][c] = "#"
            dfs(r + 1, c, node.children[temp])
            dfs(r - 1, c, node.children[temp])
            dfs(r, c + 1, node.children[temp])
            dfs(r, c - 1, node.children[temp])
            board[r][c] = temp


        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)

        return result