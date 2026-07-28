class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        min_l = min(l1, l2)

        for l in range(min_l, 0, -1):
            if l1 % l != 0:
                continue
            if l2 % l != 0:
                continue

            f1 = l1 // l
            f2 = l2 // l

            if str1[:l] * f1 == str1 and str1[:l] * f2 == str2:
                return str1[:l]

        return ""