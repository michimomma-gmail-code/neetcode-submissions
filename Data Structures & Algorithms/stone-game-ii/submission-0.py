class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        self.alice_stones = 0

        mem = {}
        def dfs(i, M):

            if (i, M) in mem:
                return mem[(i, M)]

            if i >= n:
                return 0

            max_score = - float("infinity")
            stones_taken = 0
            _score = 0
            for x in range(2 * M):
                if i + x < n:
                    stones_taken += piles[i + x]
                    nextM = max(M, x + 1)
                    score = stones_taken - dfs(i + x + 1, nextM)
                    if score > max_score:
                        max_score = score
                        
            mem[(i, M)] = max_score
            return max_score

        print('mem = ', mem)        
        relative_score = dfs(0, 1)
        total_stones = sum(piles)
        return (total_stones + relative_score) // 2        


