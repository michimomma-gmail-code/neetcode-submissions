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
        result = False
        def dfs(node, idx):
            nonlocal result
#            print(f'idx = {idx}, {len(word)}')
            if idx >= len(word):
                result = node.is_end_of_word
                return 
            for char in node.children:
#                print(char, word[idx])
                if char == word[idx] or word[idx] == ".":
                    dfs(node.children[char], idx + 1)
            return 
        
#        for c in self.root.children:
#            print(f'child = {c}')
        dfs(self.root, 0)
        return result

