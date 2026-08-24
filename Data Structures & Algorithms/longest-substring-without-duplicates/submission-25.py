class Solution:


    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        maxlen = 0
        for r in range(len(s)):
            if s[r] not in seen:
                maxlen = max(maxlen, r - l + 1)
            else:
#                print(f"seen = {seen}, r = {r}, s[r] = {s[r]}")
                while l < r and s[r] in seen:
#                    print("s[r] = ", s[r], "s[l] = ", s[l])
                    seen.remove(s[l])
                    l += 1
#            print(f'r = {r}, l = {l}')
            seen.add(s[r])
        
        return maxlen
                
    def lengthOfLongestSubstring(self, s: str) -> int:
        # index of last seen
        last_seen = {} # e.g., last_seen["a"]: 1
        # this needs to be updated once there is a dup
        # and left pointer is also updated to the previou

        max_len = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in last_seen or last_seen[s[r]] < l:
                max_len = max(max_len, r - l + 1)
            else:
                l = last_seen[s[r]] + 1

            last_seen[s[r]] = r

        return max_len

















































