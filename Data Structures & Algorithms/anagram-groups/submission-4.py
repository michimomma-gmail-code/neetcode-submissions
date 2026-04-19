class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # put all element into hashmap: key (set) -> val (list[str])

        def encode(word):
            wl = list(word)

            bucket = [0] * 26

            for w in wl:
                w_num = ord(w)-ord('a')
                bucket[w_num] += 1

            return tuple(bucket)

        anagramHP = {}

        for word in strs:
            sw = encode(word)
#            print(sw)
#            sw = "".join(sorted(word))
            
            if sw in anagramHP:
                anagramHP[sw].append(word)
            else:
                anagramHP[sw] = [word]
     
        return list(anagramHP.values())