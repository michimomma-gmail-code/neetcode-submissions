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
                return None
            cur = cur.children[w]
        return cur

    def search(self, word: str) -> bool:
        node = self._explore(word)
        if node:
            return node.is_end_of_word
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        node = self._explore(prefix)
        if node:
            return True
        else:
            return False









        













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
        
