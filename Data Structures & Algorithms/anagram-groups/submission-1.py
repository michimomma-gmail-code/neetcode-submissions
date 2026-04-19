class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # put all element into hashmap: key (set) -> val (list[str])

        anagramHP = {}

        for word in strs:
            sw = "".join(sorted(word))
            
            if sw in anagramHP:
                anagramHP[sw].append(word)
            else:
                anagramHP[sw] = [word]

        outlist = []
        for sw in anagramHP:
            outlist.append(anagramHP[sw])        
        return outlist