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
