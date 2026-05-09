class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # A->B B->C C->A
        # A->C C->B B->A

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
