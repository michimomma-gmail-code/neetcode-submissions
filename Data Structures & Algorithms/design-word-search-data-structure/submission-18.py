class TrieNode:
    def __init__(self):
#        self.val = val
        self.children = {} # {val: TreeNode}
        self.word = False

class WordDictionary:
    # root -> d -> a -> y
    #      -> b -> a -> y
    #      -> m -> a -> y
    # root.children: b (TN), b (TN), m (TN) 
    # 
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if not w in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.word = True

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(node, i):
            if i == len(word):
                return node.word

            if word[i] == ".":
                for char in node.children:
                    if dfs(node.children[char], i + 1):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)
                    
        return dfs(self.root, 0)

