class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        target = total // 4
        if total != target * 4:
            return False

        n = len(matchsticks)
        matchsticks.sort(reverse=True)

        print(f'target = {target}')

        slot = [0] * 4

        def dfs(i):
            # basecase
            if i == n:
                return True
        
            for j in range(len(slot)):
                if slot[j] >= target:
                    continue
                slot[j] += matchsticks[i]
                if slot[j] <= target:
                    if dfs(i + 1):
                        return True
                slot[j] -= matchsticks[i]
                # if slot[j] <= target:
                #dfs(i + 1)
            
            return False

        
        return dfs(0)
            
