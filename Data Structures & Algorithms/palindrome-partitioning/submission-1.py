class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        temp = []

        def dfs(cut_index):
            if cut_index >= len(s):
                result.append(temp.copy())
                return

            for j in range(cut_index, len(s)):
                if self.is_palindrome(s, cut_index, j):
                    temp.append(s[cut_index : j + 1])
                    dfs(j + 1)
                    temp.pop()

        dfs(0)
#        print(result)

        return result

    def is_palindrome(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
