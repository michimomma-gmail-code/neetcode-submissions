class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)
        print(total % 4)
        if total == 0 or total % 4 > 0:
            return False

        target = total // 4
        print(f'target = {target}')

        for m in matchsticks:
            if m > target:
                return False

        matchsticks.sort(reverse=True)
        slot = [0] * 4

        def dfs(i):
            if i == n:
                for sl in slot:
                    if sl != target:
                        return False
                print('slot = ', slot)
                return True

            for j in range(4):
                if slot[j] + matchsticks[i] > target:
                    continue
                slot[j] += matchsticks[i]
                if dfs(i + 1):
                    return True
                slot[j] -= matchsticks[i]
                if slot[j] == 0:
                    break

            return False


        res = dfs(0)
#        print(slot)
        return res
        