class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = None

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        root = TrieNode()
        for word in dictionary:
            cur = root
            for char in word:
                if char not in cur.children:
                    newnode = TrieNode()
                    cur.children[char] = newnode
                cur = cur.children[char]
            cur.end_of_word = word

        n = len(s)

        mem = {}

        def dfs(i):

            if i in mem:
                return mem[i]
            if i == n:
                return 0

            result = dfs(i + 1)

            cur = root
            for j in range(i, n):
                if s[j] in cur.children:
                    cur = cur.children[s[j]]
                    if cur.end_of_word:
                        post = dfs(j + 1)
                        result = max(result, len(cur.end_of_word) + post)
                else:
                    break

            mem[i] = result
            return result

        temp = dfs(0)
        return n - temp
                



