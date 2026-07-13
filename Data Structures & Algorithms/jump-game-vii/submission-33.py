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

            for i in range(st, ed + 1):
                if s[i] == "0":
                    if i == n - 1:
                        return True
                    queue.append(i)

            furthest = max(furthest, ed + 1)
    
        return False
                

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        n = len(s)

        dp = [False] * n
        dp[0] = True

        # [i - maxJump]   [i - minJump]       i
        available_jumps = 0
        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                available_jumps += 1
            if i >= maxJump + 1 and dp[i - maxJump - 1]:
                available_jumps -= 1

            if s[i] == "0" and available_jumps > 0:
                dp[i] = True

        return dp[n - 1]

