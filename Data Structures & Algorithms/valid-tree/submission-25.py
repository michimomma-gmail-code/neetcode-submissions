class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [ [] for _ in range(n) ]


        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        print("graph = ", graph)
        seen = set()

        def dfs(node_id, parent_id):
            if node_id in seen:
                print(f"{node_id} in seen")
                return False

            seen.add(node_id)
            print(f"seen {node_id}")

            for nei_id in graph[node_id]:
                if nei_id == parent_id:
                    continue
                if not dfs(nei_id, node_id):
                    return False

            return True

        if not dfs(0, None):
            return False

        return len(seen) == n

    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        if n == 1:
            return True

        graph = [ [] for _ in range(n) ]
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1


        print(graph)
        print(degree)

        queue = deque( [i for i in range(n) if degree[i] == 1] )
        print(queue)
        done = set()
        
        while queue:
            
            for _ in range(len(queue)):
                node = queue.popleft()
                done.add(node)

                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        queue.append(nei)


        return len(done) == n

