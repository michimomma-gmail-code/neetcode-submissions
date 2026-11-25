class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for char in s:
            seen[char] = 1 + seen.get(char, 0) 

        for char in t:
            if char in seen:
                seen[char] -= 1
                if seen[char] == 0:
                    seen.pop(char)
            else:
                return False

        if seen:
            return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for char in s:
            freq[char] = 1 + freq.get(char, 0)
        
        for char in t:
            if char not in freq:
                return False                
            freq[char] -= 1
            if freq[char] == 0:
                freq.pop(char)


        if freq:
            return False
    
        return True