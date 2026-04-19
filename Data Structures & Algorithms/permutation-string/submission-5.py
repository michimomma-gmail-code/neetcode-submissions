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
            index_r = ord(s2[r]) - ord('a')
            if freq_tab[index_r]:

                freq_tab[index_r] -= 1

                l = r - len(s1) + 1
#                print(f'l = {l}, {l - r + len(s1) + 1 }')

                idxs = []
                while l < r  :
#                    print(f'l = {l}')
                    index = ord(s2[l]) - ord('a')
                    if freq_tab[index]:
                        freq_tab[index] -= 1
                        idxs.append(index)
                    l += 1
                if len(idxs) + 1 == len(s1):
                    return True
                for i in idxs:
                    freq_tab[i] += 1

                freq_tab[index_r] += 1

        return False
