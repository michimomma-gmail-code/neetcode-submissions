from collections import defaultdict
import heapq

class Solution:

    def minCostConnectPointsU(self, points: List[List[int]]) -> int:
        # greedy connect from min-edge 
        # finish once it connect n
        n = len(points)
        edges = []

        for i in range(n):
            xi = points[i]
            for j in range(i + 1, n):
                xj = points[j]
                dij = abs(xi[0] - xj[0]) + abs(xi[1] - xj[1])
                edges.append( (dij, i, j) )

        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(p1, p2):
            root1 = find(p1)
            root2 = find(p2)

            if root1 == root2:
                return False
            else:
                if rank[p1] >= rank[p2]:
                    parent[root2] = root1
                    rank[p1] += rank[p2]
                else:
                    parent[root1] = root2
                    rank[p2] += rank[p1]

                return True

        edges.sort()

        res = 0
        count = 0
        for d, i, j in edges:
            if union(i, j):
                res += d
                count += 1
                if count == n - 1:
                    break
        return res

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)

        for i in range(n):
            xi = points[i]
            for j in range(i + 1, n):
                xj = points[j]
                dij = abs(xi[0] - xj[0]) + abs(xi[1] - xj[1])
                adj[i].append( (j, dij) )
                adj[j].append( (i, dij) )

#        start = 0

        minheap = [(0, 0)]
        visited = set()
        res = 0
        while len(visited) < n:
            #print(minheap)
            dist, node_id = heapq.heappop(minheap)
            if node_id in visited:
                continue

            res += dist
            visited.add(node_id)

            for nei, d in adj[node_id]:
#                if nei[0] not in visited:
                heapq.heappush(minheap, (d, nei) ) 
#                    visited.add(nei[0])
#                    print(visited, nei[1], nei[0], node_id)
        return res

    def minCostConnectPoints0(self, points: List[List[int]]) -> int:

        n = len(points)
        edges = []

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append( (dist, i, j) )
#                edges.append( (dist, j, i) )

        edges.sort()

        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        cost = 0
        count = 0
        for dist, i, j in edges:
            if union(i, j):
                cost += dist
                count += 1

            if count == n - 1:
                break

        return cost
        
    def minCostConnectPoints0(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append( (dist, j) )
                adj[j].append( (dist, i) )


        minheap = [ (0, 0) ]
        visited = set()

        cost = 0

        while len(visited) < n:

            dist, cur_node = heapq.heappop(minheap)

            if cur_node in visited:
                continue

            cost += dist
            visited.add(cur_node)

            for d, nei in adj[cur_node]:
                heapq.heappush(minheap, (d, nei) )


        return cost
