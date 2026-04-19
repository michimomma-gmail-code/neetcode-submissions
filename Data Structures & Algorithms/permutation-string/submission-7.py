class Solution:
    def checkInclusion0(self, s1: str, s2: str) -> bool:

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

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create final freq table for s1
        # create inital freq table for s2 -- this table will be updated during the loop
        if len(s1) > len(s2):
            return False

        freq_s1 = [0] * 26
        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            freq_s1[index] += 1

        freq_s2 = [0] * 26
        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            freq_s2[index] += 1

        match = 1
        for i in range(26):
            if freq_s2[i] != freq_s1[i]:
                match = 0
                break
    
        if match:
            return True

        match = 0
        for r in range(len(s1), len(s2)):
            index_r = ord(s2[r]) - ord('a')
            # add count of r to freq_s2
            freq_s2[index_r] += 1
            # remove count of l to freq_s2
            l = r - len(s1)
            index_l = ord(s2[l]) - ord('a')
            freq_s2[index_l] -= 1
            # match
            match = 1
            for i in range(26):
                if freq_s2[i] != freq_s1[i]:
                    match = 0
                    break        
            if match:
                return True
        
        return False

