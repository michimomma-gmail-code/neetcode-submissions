"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph0(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy

        return dfs(node) if node else None

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        oldToNew = {node: Node( node.val )}
        queue = deque( [node] )

        while queue:

            oldnode = queue.popleft()

            for nei in oldnode.neighbors:
                if not nei in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    queue.append(nei)

                oldToNew[ oldnode ].neighbors.append( oldToNew[nei] )
        
        return oldToNew[node]

