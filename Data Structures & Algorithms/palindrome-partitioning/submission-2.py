class Solution:
    def partition(self, s: str) -> List[List[str]]:
        temp = []
        result = []

        def dfs(i):
            if i >= len(s):
                result.append(temp.copy())
                return

            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    temp.append(s[i : j + 1])
                    dfs(j + 1)
                    temp.pop()


        dfs(0)

        print(result)

        return result

    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
