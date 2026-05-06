"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph_d(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        
        return dfs(node) if node else None

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        copy = Node(node.val)
        oldToNew[node] = copy

        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:

                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    queue.append(nei)

                oldToNew[cur].neighbors.append(oldToNew[nei])

        return oldToNew[node]
