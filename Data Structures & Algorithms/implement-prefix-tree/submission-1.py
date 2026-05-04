class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end_of_word = True


    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return cur.is_end_of_word


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else: 
                return False
        return True
        
        