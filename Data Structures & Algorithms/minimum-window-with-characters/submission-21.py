class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_freq = {}
        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)

        min_length = len(s)
        
        res = ""
        for r in range(len(s)):

            if s[r] in t_freq and t_freq[s[r]] > 0:
                decreased = {}

                if len(t) == 1:
                    return t

                t_freq[s[r]] -= 1
                decreased[s[r]] = 1
                l = r -1
                
                min_l = l
                num_match = 0


                while l < r and l >=0:
                    if s[l] in t_freq and t_freq[s[l]] > 0:
                        t_freq[s[l]] -= 1
                        decreased[s[l]] = 1 + decreased.get(s[l], 0)
                        min_l = min(min_l, l)
                        num_match += 1
                    l -= 1
                
#                print(f'num_match = {num_match}')
#                print(min_l)

                if num_match == len(t)-1 and min_length >= r-min_l+1:
                    s_sub = s[min_l:r+1]
                    min_length = r-min_l+1
#                    print(f'min_length = {min_length}')
#                    print(s_sub)
                    res = s_sub

                for x in decreased:
                    t_freq[x] += decreased[x]

        return res

#    def minWindow0(self, s: str, t: str) -> str:

