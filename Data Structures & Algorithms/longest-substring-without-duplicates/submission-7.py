class Solution:
    def lengthOfLongestSubstring0(self, s: str) -> int:
        # start from i, probe with j
        # store seen for the char checked s[j]
        # if s[j] in seen, remove s[j] from seen. probe with j end
        # else, add s[j] in seen, proceed (j += 1)

        max_length = 0

        for i in range(len(s)):
            seen = set()
            seen.add(s[i])
            length = 1
            j = i + 1
            while j < len(s):
                if s[j] in seen:
                    break
                else:
                    length += 1
                    seen.add(s[j])
                    j += 1
            if length > max_length:
                max_length = length

        return max_length

    def lengthOfLongestSubstring0(self, s: str) -> int:
        seen = set()

        l = 0
        max_length = 0
        for r in range(len(s)):
            char = s[r]
            while char in seen:
                seen.remove(s[l])
                l += 1
            length = r - l + 1
            max_length = max(max_length, length)
            seen.add(s[r])
        return max_length


    def lengthOfLongestSubstring1(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            length = right - left + 1
            max_length = max(max_length, length)
            seen.add(s[right])
        return max_length

        # last_seen = {}
        # left = 0
        # max_length = 0

        # for right, char in enumerate(s):
        #     if char in last_seen and last_seen[char] >= left:
        #         left = last_seen[char] + 1
        #     last_seen[char] = right
        #     max_length = max(max_length, right - left + 1)

        # return max_length


    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        seen = set()
        n = len(s)

        for right in range(n):
            char = s[right]
#            print(f'char = {char}, seen = {seen}')
            while char in seen:
                seen.remove(s[left])
                left += 1

            if char not in seen:
                seen.add(char)

            max_length = max(max_length, right - left + 1)
        
        return max_length

















