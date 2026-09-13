class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [ float("infinity") for _ in range(n)]
        adj = defaultdict(list)

        for fm_i, to_i, pr_i in flights:
            adj[fm_i].append( (to_i, pr_i) )

        queue = deque( [(src, 0)] )
        prices[src] = 0

        hops = 0
        while queue:
            lvl_len = len(queue)
            for i in range(lvl_len):
                node, price = queue.popleft()
#                if price > prices[node]:
#                    continue
                # price at hop: price 
                for n_node, n_price in adj[node]:
                    # "price + n_price" -> price at n_node (from src)
                    if price + n_price < prices[n_node]:
                        prices[n_node] = price + n_price
                        queue.append( (n_node, prices[n_node]) )
            if hops == k:
                break
            hops += 1

        return prices[dst] if prices[dst] < float("inf") else -1
        


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(dict)

        for f, t, p in flights:
            graph[f][t] = p
        # src -> dst
        minheap = []
        # (p, node, stop)
        heapq.heappush(minheap, (0, src, 0) ) 

        node_past_stop = [float("inf")] * n
        node_past_stop[src] = 0

        stop = 0

        while minheap:

            price, node, stop = heapq.heappop(minheap)

            if node == dst and stop <= k + 1:
                return price

            if stop > k + 1 or node_past_stop[node] < stop:
                continue

            node_past_stop[node] = min(node_past_stop[node], stop)

            for nei, p in graph[node].items():
                heapq.heappush(minheap, (price + p, nei, stop + 1) )
#            print("minheap   = ", minheap)


        return -1


















































