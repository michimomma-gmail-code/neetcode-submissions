class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_len = 0
        max_index = 0

        for i in range(len(s)):
            l, r = i, i

            # odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                this_len = r - l + 1
                if this_len > max_len:
                    max_len = this_len
                    max_index = l
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                this_len = r - l + 1
                if this_len > max_len:
                    max_len = this_len
                    max_index = l
                l -= 1
                r += 1

        return s[max_index: max_index + max_len]