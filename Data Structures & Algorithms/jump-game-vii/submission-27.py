class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        n = len(s)
        queue = deque([0])
        # check and move for each q in queue
        furthest = 0

        while queue:
            idx = queue.popleft()

            st = max(idx + minJump, furthest)
            ed = min(idx + maxJump, n - 1)

            if st > n - 1:
                return False

            if ed == n - 1:
                return True

            for i in range(st, ed + 1):
                if s[i] == "0":
                    queue.append(i)

            furthest = max(furthest, ed + 1)
    
        return False
                

