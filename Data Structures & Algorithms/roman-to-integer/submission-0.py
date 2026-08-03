class Solution:
    def romanToInt(self, s: str) -> int:
        s2v = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }

        val = 0
        for i in range(len(s)):
            if i + 1 < len(s) and s2v[s[i]] < s2v[s[i + 1]]:
                val -= s2v[s[i]]
            else:
                val += s2v[s[i]]

        return val