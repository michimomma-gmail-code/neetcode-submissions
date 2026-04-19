class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

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