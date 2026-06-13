class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def _startWith(self, word):
        cur = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not cur.children[index]:
                return (False, False)
            cur = cur.children[index]
        return (True, cur.endOfWord)

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        return self._startWith(word)[1]

    def startsWith(self, prefix: str) -> bool:
        return self._startWith(prefix)[0]
        
        