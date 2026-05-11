class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = defaultdict(list)

        for src, dest in tickets:
            adj[src].append(dest)

        route = []
        def dfs(city):

            while adj[city]:
                next_city = adj[city].pop()
                dfs(next_city)

            route.append(city)

        dfs("JFK")
        return route[::-1]