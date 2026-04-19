class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # put all element into hashmap: key (set) -> val (list[str])

        def encode(word):
            wl = list(word)
            count = defaultdict(int)
            for w in wl:
                count[w] += 1
            return tuple(count.items())

        anagramHP = {}

        for word in strs:
            print(encode(word))
            sw = "".join(sorted(word))
            
            if sw in anagramHP:
                anagramHP[sw].append(word)
            else:
                anagramHP[sw] = [word]
     
        return list(anagramHP.values())