class Solution:
    def isPalindrome_0(self, s: str) -> bool:

        s = ''.join(c.lower() for c in s if c.isalnum())

        for i in range(len(s)//2):
            c = s[i]
            i_rev = len(s)-1 - i
            if not c == s[i_rev]:
                return False
        return True

    def isPalindrome_rev(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c.lower() for c in s if c.isalnum())

        l = 0
        r = len(s)-1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
