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
        # adj = defaultdict(list)
        # run traverse, derive the ordering
        # record the order for each course, finally evaluate queries

        adj = [ [] for _ in range(numCourses) ]
        indegree = [0] * numCourses

        for pre, crs in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        current = [i for i in range(numCourses) if indegree[i] == 0 ]

        # BFS
#        seen = set()
#        order = [numCourses] * numCourses
        queue = deque(current)
#        print(queue)
        allpr = [ set() for _ in range(numCourses) ]
        print(allpr)
        lvl = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
#                order[node] = lvl
                for nxt in adj[node]:
                    allpr[nxt].add(node)
                    allpr[nxt].update(allpr[node])
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
            lvl += 1

#        print(order)

        res = [ pre in allpr[crs] for pre, crs in queries ]
        return res
