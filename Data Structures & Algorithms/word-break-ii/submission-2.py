class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordDict_s = set(wordDict)
        memo = {}

        n = len(s)

        def dfs(left):

            if left in memo:
                return memo[left]

            if left == n:
#                result.append(" ".join(temp))
                return [""]

            valid_sentences = []
            for j in range(left, n):

                word = s[left:(j + 1)]
                if word in wordDict_s:
#                    temp.append(s[left:(j + 1)])
                    suffix_sentences = dfs(j + 1)
                    for suffix in suffix_sentences:
                        if suffix == "":
                            valid_sentences.append(word)
                        else:
                            valid_sentences.append(word + " " + suffix)
#                    temp.pop()
            memo[left] = valid_sentences
            return valid_sentences
            
        return dfs(0)

