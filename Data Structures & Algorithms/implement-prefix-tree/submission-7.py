class TrieNode:
    def __init__(self):
        self.children = {} # {char: TrieNode}
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if not w in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.is_end_of_word = True

    def _explore(self, word):
        cur = self.root
        for w in word:
            if not w in cur.children:
                return (False, False)
            cur = cur.children[w]
        return (True, cur.is_end_of_word)

    def search(self, word: str) -> bool:
        res = self._explore(word)
        return res[1]


    def startsWith(self, prefix: str) -> bool:
        res = self._explore(prefix)
        return res[0]









        













# class PrefixTree:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         cur = self.root
#         for char in word:
#             if char not in cur.children:
#                 cur.children[char] = TrieNode()
#             cur = cur.children[char]
#         cur.is_end_of_word = True


#     def search(self, word: str) -> bool:
#         cur = self.root
#         for char in word:
#             if char not in cur.children:
#                 return False
#             cur = cur.children[char]

#         return cur.is_end_of_word


#     def startsWith(self, prefix: str) -> bool:
#         cur = self.root
#         for char in prefix:
#             if char not in cur.children:
#                 return False
#             cur = cur.children[char]

#         return True
        
