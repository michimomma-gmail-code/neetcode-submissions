class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict_s = set(wordDict)
        n = len(s)

        mem = {}

        def dfs(i):

            if i in mem:
                return mem[i]

            if i == n:
                return [""]

            sentences = []
            for j in range(i, n):
                word = s[i: (j + 1)]

                if word in wordDict_s:

                    suffix = dfs(j + 1)
                    for suf in suffix:
                        if suf == "":
                            sentences.append(word)
                        else:
                            sentences.append(word + " " + suf)
            mem[i] = sentences
            return sentences

        return dfs(0)

