class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append( (v, w) )

        min_heap = [ (0, k) ]

        visited = set()

        maxtime = 0

        while min_heap:

            time, node = heapq.heappop(min_heap)

            if node in visited:
               continue

            visited.add(node)
            maxtime = max(maxtime, time)

            for nei, dt in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + dt, nei) )


        if len(visited) < n:
            return -1

        return maxtime



