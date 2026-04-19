class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c.lower() for c in s if c.isalnum())

        for i, c in enumerate(s):
            if i > len(s)//2:
                break
            i_rev = len(s)-1 - i
            if not c == s[i_rev]:
                return False
        return True

