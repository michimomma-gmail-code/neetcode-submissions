class Solution:
    def longestPalindromeP(self, s: str) -> str:
        

        def twoPtrSearch(l, r):
            max_len = 0
            max_index = 0
#            l, r = i, i + 1
#            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                this_len = r - l + 1
                if this_len > max_len:
                    max_len = this_len
                    max_index = l
                l -= 1
                r += 1
            return max_index, max_len

        max_len = 0
        max_index = 0
        for i in range(len(s)):
            max_index_even, max_len_even = twoPtrSearch(i, i + 1)
            max_index_odd, max_len_odd = twoPtrSearch(i, i)
            if max_len_even > max_len:
                max_len = max_len_even
                max_index = max_index_even
            if max_len_odd > max_len:
                max_len = max_len_odd
                max_index = max_index_odd

            # even

        return s[max_index: max_index + max_len]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        dp = [ [False] * n for _ in range(n) ]

        longest_start = 0
        max_len = 1

        # base case
        for i in range(n):
            dp[i][i] = True

        # length = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest_start = i
                max_len = 2

        # length >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_len:
                        longest_start = i
                        max_len = length

#        print(f'longest_start = {longest_start}, max_len = {max_len}')
        return s[longest_start : longest_start + max_len]


