class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    
        adj = [ [] for _ in range(n) ]
        degree = [0] * n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            adj[u].append(v)
            adj[v].append(u)

        queue = deque([i for (i, deg) in enumerate(degree) if deg <= 1])
#        print(degree)
        seen = set()
#        print(queue)
        remaining_node = n
        while remaining_node > 2:
            
            remaining_node -= len(queue)

            for _ in range(len(queue)):
                node = queue.popleft()
                degree[node] -= 1
                seen.add(node)

                for nei in adj[node]:
                    if nei in seen:
                        continue
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        queue.append(nei)

        print(f'degree = {degree}, queue = {queue}')
        return list(queue)                