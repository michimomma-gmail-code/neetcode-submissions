class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # prerequisites[i] = [ai, bi]: ai -> bi
        #
        # a -> b -> c
        #
        # queries[j] = [uj, vj]
        # ui -> vj?
        #
        # prerequisites = [[1,0],[2,1],[3,2]]
        # 1 -> 0, 2 -> 1, 3 -> 2 : 3 -> 2 -> 1 -> 0
        # 
        # [0, 1] false
        # [3, 1] true

        # list of list
#        adj = defaultdict(list)
        adj = [ [] for _ in range(numCourses) ]

        for pre, crs in prerequisites:
            adj[pre].append(crs)

        print(adj)

        def dfs(node, target):
            if node == target:
                return True
            if not adj[node]:
                return False
            for crs in adj[node]:
                if not crs in visited:
                    visited.add(crs)
                    if dfs(crs, target):
                        return True
            return False

        res = []
        for pre, crs in queries:
            visited = set()
            res.append( dfs(pre, crs) )

        return res

