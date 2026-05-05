class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
#            print(f'idx = {idx}, {len(word)}')
            if idx >= len(word):
                result = node.is_end_of_word
                return result
            for char in node.children:
#                print(char, word[idx])
                if char == word[idx] or word[idx] == ".":
                    if dfs(node.children[char], idx + 1):
                        return True
            return False
        
#        for c in self.root.children:
#            print(f'child = {c}')
        return dfs(self.root, 0)

