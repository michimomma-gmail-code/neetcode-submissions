"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
#    def cloneGraph_d(self, node: Optional['Node']) -> Optional['Node']:
        
    #     oldToNew = {}

    #     def dfs(node):
    #         if node in oldToNew:
    #             return oldToNew[node]

    #         copy = Node(node.val)
    #         oldToNew[node] = copy

    #         for nei in node.neighbors:
    #             copy.neighbors.append(dfs(nei))

    #         return copy

        
    #     return dfs(node) if node else None

    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if not node:
    #         return None

    #     oldToNew = {}

    #     oldToNew[node] = Node(node.val)

    #     queue = deque([node])

    #     while queue:
    #         cur = queue.popleft()
    #         for nei in cur.neighbors:

    #             if nei not in oldToNew:
    #                 oldToNew[nei] = Node(nei.val)
    #                 queue.append(nei)

    #             oldToNew[cur].neighbors.append(oldToNew[nei])

    #     return oldToNew[node]


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = set()
        old2new = {node: Node(node.val)}

        def dfs(node):
            if not node:
                return
            if node in visited:
                return
#            print("node val = ", node.val)
            newnode = old2new[node]
            visited.add(node)

            for j, nei in enumerate(node.neighbors):
#                print("j = ", j, "val = ", nei.val)
                if nei not in old2new:
                    newnei = Node(nei.val)
                    old2new[nei] = newnei
                else:
                    newnei = old2new[nei]

                newnode.neighbors.append(newnei)

                dfs(nei)
            
            return 

        dfs(node)

        return old2new[node]







































