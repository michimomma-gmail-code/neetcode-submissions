class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for fm_i, to_i, pr_i in flights:
            adj[fm_i].append( (to_i, pr_i) )

        done = set()
        # minheap: (price, node, hop)
        minheap = [ (0, src, 0) ]

        # k = 1, means src -> () -> dest: doing 2 times (k + 1)
        for h in range(1, k + 3):
            print(f'out start: minheap = {minheap}, done = {done}')
            # within level 
            for i in range( len(minheap) ):
                price, node, p_hop = heapq.heappop(minheap)
                print(f'running price, node, p_hop = {price},{node},{p_hop}')
                if node in done:
                    continue

                done.add(node)
                if node == dst:
                    return price

                for nnode, nprice in adj[node]:
                    print(f'trying to push {nnode} with price {nprice}: ({nprice}, {nnode}, {p_hop + 1})')
                    if nnode in done or p_hop + 1 > k + 1:
                        if nnode in done:
                            print(f'node {nnode} skipped as done')
                        else:
                            print(f'node {node} skiiped as p_hop + 1 = {p_hop + 1}')
                        continue
                    heapq.heappush(minheap, (price + nprice, nnode, p_hop + 1) )

        # not done by k + 1 contraint
        print(f'loop ended - remainder is {minheap}, done = {done}')
        while minheap:
            p, n, h = heapq.heappop(minheap)
            if n == dst and h < k+1:
                return p

        return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(dict)
        for fm, to, pr in flights:
            adj[fm][to] = pr

        node_cost = [float("inf")] * n

        queue = deque([ (src, 0) ])
        node_cost[src] = 0

        stops = -1
        while queue:
            if stops == k:
                break
            for _ in range(len(queue)):
                node, cost = queue.popleft()
                    
                for nei, pr in adj[node].items():
                    nei_cost = cost + pr
                    if nei_cost < node_cost[nei]:
                        node_cost[nei] = nei_cost
                        queue.append( (nei, nei_cost) )

            stops += 1
        
        if node_cost[dst] < float("inf"):
            return node_cost[dst]
        else:
            return -1