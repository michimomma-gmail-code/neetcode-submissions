sys.setrecursionlimit(10**5) # Increases limit to 100,000
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        mem = {}
        def dfs(i):
            if i >= n:
                return 0
            if i in mem:
                return mem[i]
            max_score = -float("infinity")
            stone_taken = 0

            for k in range(1, 4):
                if i + k - 1 < n:
                    stone_taken += stoneValue[i + k - 1]
                    max_score = max(max_score, stone_taken - dfs(i + k))
            
            mem[i] = max_score
            return max_score

        
        score = dfs(0)
        if score > 0: return "Alice"
        elif score < 0: return "Bob"
        else: return "Tie"

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [- float("infinity")] * (n + 1)
        dp[n] = 0

        for i in range(n, -1, -1):
            stones_taken = 0
            for k in range(1, 4):
                if i + k - 1 < n:
                    stones_taken += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], stones_taken - dp[i + k])

        if dp[0] > 0: return "Alice"
        elif dp[0] < 0: return "Bob"
        else: return "Tie"

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dfs(i)
        # score = stones_taken (k: 1-3) - dfs(i + k)

        k = 3
        n = len(stoneValue)

        mem = {}

        def dfs(i):
            if i in mem:
                return mem[i]
            if i >= n:
                return 0
            stones_taken = 0
            max_score = - float("infinity")
            for j in range(k):
                if i + j < n:
                    stones_taken += stoneValue[i + j]
                    max_score = max(max_score, stones_taken - dfs(i + j + 1))
            
            mem[i] = max_score
            return max_score

        res = dfs(0)
        print(res)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie" 

