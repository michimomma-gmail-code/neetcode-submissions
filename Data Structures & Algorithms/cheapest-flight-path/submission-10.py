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
        