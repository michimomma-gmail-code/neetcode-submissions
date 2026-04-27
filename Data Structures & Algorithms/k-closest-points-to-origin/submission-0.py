class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data = [(math.sqrt(x**2 + y**2), [x, y]) for (x,y) in points]

        heapq.heapify(data)

        res = []
        while len(res) < k:
            min_elem = heapq.heappop(data)
            res.append(min_elem[1])

        return res