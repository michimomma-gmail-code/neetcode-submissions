class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start from i, probe with j
        # store seen for the char checked s[j]
        # if s[j] in seen, remove s[j] from seen. probe with j end
        # else, add s[j] in seen, proceed (j += 1)

        seen = set()
        length = 0
        max_length = length
        for i in range(len(s)):
            seen = set()
            seen.add(s[i])
            length = 1
            j = i + 1
            while j < len(s):
                if s[j] in seen:
#                    seen.discard(s[j])
                    break
                else:
                    length += 1
                    seen.add(s[j])
                    j += 1
#                print(f'i={i}, seen={seen}, length={length}')   
            if length > max_length:
                max_length = length

        return max_length
