class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        result = []

        wordDict_s = set(wordDict)
        temp = []

        n = len(s)

        def dfs(left):
            if left == n:
                result.append(" ".join(temp))
            for j in range(left, n):
                
                if s[left:(j + 1)] in wordDict_s:
                    temp.append(s[left:(j + 1)])
                    dfs(j + 1)
                    temp.pop()

            
        dfs(0)

        return result