class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # node -> neighbor
        #
        graph = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w

        print(graph)
        minheap = []

        start = k
        heapq.heappush(minheap, (0, start) )

#        print(minheap)
        visited = set()
        res = 0
        while minheap:
            w, node = heapq.heappop(minheap)
            if node in visited:
                continue

            visited.add(node)
            res = max(w, res)
#            print(node, w)
                
            for nei, nei_w in graph[node].items():
                heapq.heappush(minheap, (w + nei_w, nei))

#        print(visited)

        if len(visited) == n:
            return res
        else:
            return -1
        