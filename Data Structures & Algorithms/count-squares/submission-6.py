class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
#        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
#        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), diag_counts in self.ptsCount.items():
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += diag_counts * self.ptsCount.get((x, py), 0) * self.ptsCount.get((px, y), 0)
        return res

#     def __init__(self):
#         self.points = {}

#     def add(self, point: List[int]) -> None:
#         x, y = point
#         self.points[(x, y)] = 1 + self.points.get( (x,y), 0)


        
#     def count0(self, point: List[int]) -> int:
# #        print(self.points)
#         qx, qy = point

#             # other point: 
#             # (qx, qy), (x, y), 
#             # dianogal: (qx, y), (x, qy)
#             # qx = x: x + (qy - y), or x -(qy - y) for y and qy
#             # qy = y: y + (qx - x), or y -(qx - x) for x and qx
            

#         is_square = False
#         self_dup = 0

#         res = 0

#         for x, y in self.points:
#             if (qx, qy) == (x, y):
#                 self_dup = 2
#             else:
#                 self_dup = 1
#             dx, dy = x - qx, y - qy
#             if not(x == qx or y == qy or dx == dy):
#                 break
#             if dx == dy:
#                 if (qx, y) in self.points and (x, qy) in self.points:
#                     res += self.points((qx, y)) * self.points( (x, qy) ) * self_dup

            

#         if not is_square:
#             return 0

#         return res
