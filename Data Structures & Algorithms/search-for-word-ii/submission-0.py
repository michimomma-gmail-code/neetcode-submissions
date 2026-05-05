class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

#        print(f'root.children = {root.children.keys()}')

        result = []

        nrows, ncols = len(board), len(board[0])

        def dfs(r, c, node):

            if (r < 0 or c < 0 or r >= nrows or c >= ncols 
                or board[r][c] not in node.children):
                return False

            temp = board[r][c]
            current_node = node.children[temp]

            if current_node.word:
                result.append( current_node.word )
                current_node.word = None

            board[r][c] = "#"
            dfs(r + 1, c, current_node)
            dfs(r - 1, c, current_node)
            dfs(r, c + 1, current_node) 
            dfs(r, c - 1, current_node)
            board[r][c] = temp
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, root)
            
        return result
