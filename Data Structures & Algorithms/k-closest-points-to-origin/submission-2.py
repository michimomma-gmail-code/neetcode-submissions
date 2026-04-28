class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        data = []
        for idx, (x, y) in enumerate(points):
            dist = x**2 + y**2
            if idx <= k - 1:
                _ = ( -dist, x, y)
                data.append(_)

            if idx == k - 1:
#                    print(f'data = {data}')
                    heapq.heapify(data)
            elif idx > k - 1:
#                print(f'data = {data}')
                max_v = -data[0][0]
                if dist < max_v:
                    heapq.heapreplace(data, (-dist, x, y))
#        data = [ (x**2 + y**2, x, y) for (x,y) in points]

        res = [(x, y) for negdist, x, y in data]

        return res