import sys
sys.setrecursionlimit(10**5) # Increase the limit to 100,000
class Solution:
    def longestIncreasingPathD(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        memo = [ [0] * n for _ in range(m) ]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if memo[r][c] > 0:
                return memo[r][c]

            max_len = 1
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < m and 0 <= new_c < n and matrix[r][c] < matrix[new_r][new_c]:
                    max_len = max(max_len, dfs(new_r, new_c) + 1)

            memo[r][c] = max_len

            return max_len

        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        
        return res

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        in_degree = [ [0] * n for _ in range(m) ]

        for r in range(m):
            for c in range(n):
                temp = 0
                for dr, dc in directions:
                    nei_r, nei_c = r + dr, c + dc
                    if nei_r < 0 or nei_r >= m or nei_c < 0 or nei_c >= n:
                        continue
                    if matrix[r][c] > matrix[nei_r][nei_c]:
                        temp += 1
                in_degree[r][c] = temp
        
        queue = deque()
        for r in range(m):
            for c in range(n):
                if in_degree[r][c] == 0:
                    queue.append( (r, c) )

        print(in_degree)

        done = set()
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
#                done.add( (r, c) )
                for dr, dc in directions:
                    nei_r, nei_c = r + dr, c + dc
                    if nei_r < 0 or nei_r >= m or nei_c < 0 or nei_c >= n:
                        continue

                    if matrix[r][c] < matrix[nei_r][nei_c]:
                        in_degree[nei_r][nei_c] -= 1
                        if in_degree[nei_r][nei_c] == 0:
                            queue.append( (nei_r, nei_c) )

        return count

