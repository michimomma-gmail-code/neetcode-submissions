class Solution:

    def isPalindrome(self, s: str) -> bool:
        def alphanum(c):

            return (ord("a") <= ord(c.lower()) <= ord("z") or ord("0") <= ord(c) <= ord("9"))

        l, r = 0, len(s) - 1

        while l <= r:
            if not alphanum(s[l]):
                l += 1
                continue
            if not alphanum(s[r]):
                r -= 1
                continue
#            print(s[l : r + 1])
            if not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1

        return True
        
