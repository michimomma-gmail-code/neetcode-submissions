class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [ [] for _ in range(numCourses) ]


        for crs, pre in prerequisites:
            graph[crs].append(pre)

        print("graph = ", graph)

        visit = set()

        def dfs(node):
            # if not graph[node]:
            #     return True

            if node in visit:
                return False

            visit.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visit.remove(node)
            graph[node] = []

            return True

        print("graph = ", graph)

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
    
