class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_freq = {}
        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)

        min_length = len(s)
        
        res = ""
        for r in range(len(s)):

            if s[r] in t_freq and t_freq[s[r]] > 0:
                decreased = {}

                if len(t) == 1:
                    return t

                t_freq[s[r]] -= 1
                decreased[s[r]] = 1
                l = r -1
                
                min_l = l
                num_match = 0


                while l < r and l >=0:
                    if s[l] in t_freq and t_freq[s[l]] > 0:
                        t_freq[s[l]] -= 1
                        decreased[s[l]] = 1 + decreased.get(s[l], 0)
                        min_l = min(min_l, l)
                        num_match += 1
                    l -= 1
                
#                print(f'num_match = {num_match}')
#                print(min_l)

                if num_match == len(t)-1 and min_length >= r-min_l+1:
                    s_sub = s[min_l:r+1]
                    min_length = r-min_l+1
#                    print(f'min_length = {min_length}')
#                    print(s_sub)
                    res = s_sub

                for x in decreased:
                    t_freq[x] += decreased[x]

        return res

    def minWindow_(self, s: str, t: str) -> str:

        if t == "":
            return ""

        t_freq, window = {}, {}

        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)

        min_length = float("infinity")
        res = [-1, -1]
        
        have, need = 0, len(t_freq)
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_freq and window[c] == t_freq[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < min_length:
                    res = [l, r]
                    min_length = r - l + 1
                # move l (l -> l+1)
                window[s[l]] -= 1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
        l, r = res
#        print(res)
        return s[l:r+1] if min_length != float("infinity") else ""


    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        t_freq = Counter(t)
        needed = len(t_freq)
        in_window = {}
        have = 0
        min_idx = [0, float("inf")]
        l = 0
        for r in range(len(s)):
#            print(f"s[r] = {s[r]}")
            if s[r] in t_freq:
                in_window[s[r]] = 1 + in_window.get(s[r], 0)
                if in_window[s[r]] == t_freq[s[r]]:
                    have += 1
                if have == needed:
                    # found a sol
#                    print("met", s[l : (r + 1)])
                    if (min_idx[1] - min_idx[0] + 1) > (r - l + 1):
                        min_idx = [l, r]
                    # break the sol, and proceed for next sol
                    while l < r and have == needed:
                        if s[l] in t_freq:
                            in_window[s[l]] -= 1
                            if in_window[s[l]] < t_freq[s[l]]:
                                have -= 1
                        l += 1
                # elif s[l] == s[r] and in_window[s[l]] > t_freq[s[l]]:
                #     l += 1
                while l <= r:
                    if s[l] in t_freq:
                        if in_window[s[l]] > t_freq[s[l]]:
                            in_window[s[l]] -= 1
                        else:
                            break
                    l += 1

            while l <= r and s[l] not in t_freq:
                l += 1
#            print('current = ', s[l : (r + 1)])

        if min_idx[1] == float("inf"):
            return ""

        return s[min_idx[0] : (min_idx[1] + 1)]







































