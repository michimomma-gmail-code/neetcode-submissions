class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # [[2,1], [1,3]]
        # 2 -> 1
        # 1 -> 3
        # [[3,1], [2,3]]
        # 3 -> 1
        # 2 -> 3
        # k x k 

        def toposort(cond):
    #        cond = rowConditions
            adj = defaultdict(list)
            in_degree = [0] * k

            for fm, to in cond:
                fm -= 1
                to -= 1
                in_degree[to] += 1
                adj[fm].append(to)
            
#            print('in_degree = ', in_degree, 'adj = ', adj)
            queue = deque( [ i for i in range(k) if in_degree[i] == 0] )
            res = list(queue)
            seen = set(queue)

            while queue:
                for _ in range(len(queue)):
                    idx = queue.popleft()
                    for nxt_idx in adj[idx]:
                        if nxt_idx in seen:
                            continue
                        in_degree[nxt_idx] -= 1
                        if in_degree[nxt_idx] == 0:
                            seen.add(nxt_idx)
                            res.append(nxt_idx)
                            queue.append(nxt_idx)

            return res

        row_idx = toposort(rowConditions)
        col_idx = toposort(colConditions)

        if not row_idx or not col_idx:
            return []

        print(row_idx, col_idx)
        res = [ [0] * k for _ in range(k) ]
        # [1, 0, 2] [1, 2, 0] 2 -> 0, 3 -> 1, 1 -> 2
        col_rev = {col_idx[i] : i for i in range(k)}
        print('col_rev = ', col_rev)
        #
        # [2, 0, 0] (0,0)
        # [0, 0, 1] (1,2)
        # [0, 3, 0] (2,1)

        for i in range(k):
            r = row_idx[i]
            c = col_rev[r]
            r1 = r + 1
            res[i][c] = r1

        return res

