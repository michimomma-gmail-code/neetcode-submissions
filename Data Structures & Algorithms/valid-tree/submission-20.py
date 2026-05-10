class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
#        if not edges:
#            return n == 1
        if len(edges) != n - 1:
            return False        
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visiting = set()

        def dfs(node, parent):

            if node in visiting:
                return False

            visiting.add(node)

            for nei in graph[node]:

                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, None):
            return False

        return len(visiting) == n
