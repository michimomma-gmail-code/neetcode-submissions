class Solution:
    def longestPalindromeP(self, s: str) -> str:
        

        def twoPtrSearch(l, r):
            max_len = 0
            max_index = 0
#            l, r = i, i + 1
#            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l + 1 - 2


        max_len = 0
        max_index = 0
        for i in range(len(s)):
            max_len_even = twoPtrSearch(i, i + 1)
            max_len_odd = twoPtrSearch(i, i)
            if max_len_even > max_len:
                max_len = max_len_even
                # index i - len / 2
                # len = 2, [i][i+1]
                # i - (2 - 1) // 2
                # len 3, [i-1][i][i+1]
                # i - (3 -1) // 2 = i -1
                max_index = i - (max_len - 1) // 2
            if max_len_odd > max_len:
                max_len = max_len_odd
                max_index = i - (max_len - 1) // 2


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
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_len:
                        longest_start = i
                        max_len = length

#        print(f'longest_start = {longest_start}, max_len = {max_len}')
        return s[longest_start : longest_start + max_len]


    def longestPalindrome(self, s: str) -> str:

        def search(l, r):
            # even: a a (l = r -1)
            # odd: a b a (l = r)

            while 0 <= l and r < len(s) and l <= r and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1
            r -= 1
            w = r - l + 1
            return (l, r, w)

        max_w = 0
        left, right = 0, 0
        for i in range(len(s)):
            # even
            l_e, r_e, w_e = search(i, i)
            if w_e > max_w:
                max_w = w_e
                left, right = l_e, r_e

            if i < len(s):
                # odd
                l_o, r_o, w_o = search(i, i + 1)
                if w_o > max_w:
                    max_w = w_o
                    left, right = l_o, r_o
#            print(max_w, s[i], w_e, w_o, left, right)

            
        return s[left : (right + 1)]























































