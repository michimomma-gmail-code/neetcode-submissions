class Solution:
    def canFinish0(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def buildGraph(prerequisites):
            preG = defaultdict(list)
            for source, dest in prerequisites:
                preG[source].append(dest)
            return preG

        preG = buildGraph(prerequisites)

#        print(preG)

        visited = set()
        done = set()

        def dfs(pre):
#            print(preG)
            if pre in done:
                return True
            if pre in visited:
                return False
            visited.add(pre)
#            print(visited)
            for course in preG[pre]:
                if not dfs(course):
                    return False

            visited.remove(pre)
            done.add(pre)

            return True
        
        # for pre in list(preG.keys()):
        #     if not dfs(pre):
        #         return False
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):

            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
#            print(visited)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            preMap[crs] = []

            return True
        
        # for pre in list(preG.keys()):
        #     if not dfs(pre):
        #         return False
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisite = [a, b]: a -> b
        #

        graph = [ [] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for pre, crs in prerequisites:
            graph[pre].append(crs)
            indeg[crs] += 1
        print("graph = ", graph)
        print("indeg = ", indeg)

#        ready = [crs for crs in indeg if indeg[crs] == 0]
        ready = [i for i in range(numCourses) if indeg[i] == 0]
        # for i in range(numCourses):
        #     if indeg[i] == 0:
        #         ready.append(i)

        queue = deque(ready)

        while queue:
            for _ in range(len(queue)):
                crs = queue.popleft()
                neighbours = graph[crs]
                for nei in neighbours:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        queue.append(nei)

        return sum(indeg) == 0

















