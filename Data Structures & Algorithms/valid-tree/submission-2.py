class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        print(graph)
        visiting = set()
        visitingEdge = set()
        done = set()
        def dfs(node):
            print(f'node = {node}')

            if node in done:
                return True

            if node in visiting:
                print(node, visiting)
                return False

            visiting.add(node)

            for nei in graph[node]:
                print(f'nei = {nei}')
                if (min(node, nei), max(node,nei)) in visitingEdge:
                    continue
                else:
                    visitingEdge.add( ( min(node, nei), max(node,nei) ))
                if not dfs(nei):
                    return False

            visiting.remove(node)
            done.add(node)

            return True

        for node in list(graph.keys()):
            print(f'start node = {node}')

            if not dfs(node):
                return False
            break
        
        if len(done) < len(graph.keys()):
            return False
        return True