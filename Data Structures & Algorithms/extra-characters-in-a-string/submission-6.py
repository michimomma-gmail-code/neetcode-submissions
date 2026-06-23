class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        # build Trie
        root = TrieNode()
        for word in dictionary:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.word = word

        
        n = len(s)
        mem = {}
        # return max chars covered (starting i)
        def dfs(i):
            if i in mem:
                return mem[i]

            if i == n:
                return 0

            res = dfs(i + 1)

            cur = root
            for j in range(i, n):
                # try to match word
                if s[j] in cur.children:
                    cur = cur.children[s[j]]
                    if cur.word:
                        res = max(res, len(cur.word) + dfs(j + 1)) 
                else:
                    break
               
            mem[i] = res
            return res
    
        return n - dfs(0)