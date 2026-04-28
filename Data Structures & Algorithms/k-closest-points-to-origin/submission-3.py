class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        data = [ (-(x**2 + y**2), x, y) for (x, y) in points[:k]]
        heapq.heapify(data)

        for i in range(k, len(points)):
            x, y = points[i]
            dist = x**2 + y**2
            max_v = -data[0][0]
            if dist < max_v:
                heapq.heapreplace(data, (-dist, x, y))

        res = [(x, y) for negdist, x, y in data]

        return res