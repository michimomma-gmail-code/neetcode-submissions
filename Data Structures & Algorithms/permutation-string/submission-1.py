class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        freq_tab = [0] * 26

        for c1 in s1:
            freq_tab[ord(c1)-ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            print(f'r = {r}')
            if freq_tab[ord(s2[r]) - ord('a')]:

                freq_tab[ord(s2[r]) - ord('a')] -= 1

                l = r - len(s1) + 1
#                print(f'l = {l}, {l - r + len(s1) + 1 }')

                ls = []
                while l < r  :
#                    print(f'l = {l}')
                    if freq_tab[ord(s2[l]) - ord('a')]:
                        freq_tab[ord(s2[l]) - ord('a')] -= 1
                        ls.append(l)
                    l += 1
                if len(ls) + 1 == len(s1):
                    return True
                for i in ls:
                    freq_tab[ord(s2[i]) - ord('a')] += 1

                freq_tab[ord(s2[r]) - ord('a')] += 1

        return False
