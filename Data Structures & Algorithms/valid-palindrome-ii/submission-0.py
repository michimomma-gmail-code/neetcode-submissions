class Solution:
    def validPalindrome(self, s: str) -> bool:
        # abbda
        # abccda
        def isValid(l, r, itr):
            if itr > 1:
                return False

            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if isValid(l, r - 1, itr + 1) or isValid(l + 1, r, itr + 1):
                        return True
                    else:
                         return False
            return True

        return isValid(0, len(s) - 1, 0)

