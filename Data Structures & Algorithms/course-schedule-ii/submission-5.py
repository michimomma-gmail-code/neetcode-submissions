class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [course, pre]
        # order of courses: pre -> course

        #pre2course = {i : [] for i in range(numCourses)}
#        pre2course = {p: [] for (p, c) in prerequisites}
        pre2course = defaultdict(list)
        for c, p in prerequisites:
            pre2course[p].append(c)
#        print(pre2course)
        visiting = set()
        done = set()
        res = []

        def dfs(pre):
            #loop
            if pre in done:
                return True
            if pre in visiting:
                return False
            
            visiting.add(pre)
            
            for crs in pre2course[pre]:
                if not dfs(crs):
                    return False
            
            done.add(pre)
            res.append(pre)
#            print(visiting)
            visiting.remove(pre)
            return True

        for pre in list(pre2course):
            if not dfs(pre):
                return []

        result = []
        while res:
            result.append(res.pop())
        indep = [i for i in range(numCourses) if i not in done]
        result.extend(indep)
        
        return result







