"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

#        root = Node()
#       unit = (r, c, num) 
#       r, c in (0, 1, 2, ..., num - 1) -- most granular level
#       r, c in (0), (0, 4), (0, 2, 4, 6), etc. 
#

        def dfs(r, c, num):
            
            if num == 1:
                val = grid[r][c]
                node = Node(val == 1, True)
                return node

            d = num // 2
            topleft = dfs(r, c, d)
            topright = dfs(r, c + d, d)
            bottomleft = dfs(r + d, c, d)
            bottomright = dfs(r + d, c + d, d)

            if topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and topleft.val == topright.val == bottomleft.val == bottomright.val:
                return Node(topleft.val, True)
            
            return Node(False, False, topleft, topright, bottomleft, bottomright)
            

        return dfs(0, 0, n)

