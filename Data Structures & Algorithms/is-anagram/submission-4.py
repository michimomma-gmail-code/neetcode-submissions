class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict()
        for v in s:
            count[v] = count.get(v, 0) + 1
        
        for v_t in t:
            if v_t not in count:
                return False
            count[v_t] = count.get(v_t, 0) - 1

        for v in count:
            if count[v] > 0:
                return False

        return True