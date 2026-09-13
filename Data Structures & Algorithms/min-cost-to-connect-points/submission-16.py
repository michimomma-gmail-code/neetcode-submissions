class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(pi, pj):
            n = len(pi)
            res = 0
            for _ in range(n):
                res += abs( pi[_] - pj[_])
            return res

        m = len(points)

        adj = [ [] for _ in range(m) ]

        for i in range(m):
            for j in range(i + 1, m):
                d = dist(points[i], points[j])
                adj[i].append( (j, d) )
                adj[j].append( (i, d) )

        minheap = []
        # init: point 0, dist = 0
        heapq.heappush(minheap, (0, 0) ) # (d, point_id)
        seen = set()
        res = 0

        while minheap:
            dist, pt = heapq.heappop(minheap)
            if pt in seen:
                continue
            seen.add(pt)
#            print(seen)
            res += dist
            if len(seen) == m:
                return res

            for nei, nei_d in adj[pt]:
                cur_d = nei_d
                heapq.heappush( minheap, (cur_d, nei) )
            


