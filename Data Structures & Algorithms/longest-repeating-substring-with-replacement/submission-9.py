class Solution:
    def characterReplacement_(self, s: str, k: int) -> int:

        max_length = 0
        freq_tab = {}
        max_freq = 0
        l = 0
        for r in range(len(s)):
            freq_tab[s[r]] = 1 + freq_tab.get(s[r], 0)
            max_freq = max(max_freq, freq_tab[s[r]])

            while r - l + 1 - max_freq > k:
                freq_tab[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
        
        return max_length

    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(s)
        res = 0
        for c in charset:
            c_count = 0
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    c_count += 1
                while r - l + 1 - c_count > k:
                    if s[l] == c:
                        c_count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res



    def characterReplacement(self, s: str, k: int) -> int:
    #    "X Y Y X"
    #     0 1 2 3 
    #     X
    #     window_size (r - l + 1) <=  max_freq + k -- occupied (max_freq + k is cur sol)
    #     window_size (r - l + 1) >  max_freq + k  -- not 
        
        freq = {}
        max_freq = 0
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            max_freq = max(max_freq, freq[s[r]])

            while (r - l + 1) > (max_freq + k):
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res







































