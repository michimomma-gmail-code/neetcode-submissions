class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = defaultdict()
        for v in s:
            s_count[v] = s_count.get(v, 0) + 1
        
        print(s_count)

        t_count = defaultdict()
        for v_t in t:
            if v_t not in s_count:
                return False
            t_count[v_t] = t_count.get(v_t, 0) + 1

        print(t_count)
        
        for v in s:
            if t_count[v] != s_count[v]:
                return False

        return True