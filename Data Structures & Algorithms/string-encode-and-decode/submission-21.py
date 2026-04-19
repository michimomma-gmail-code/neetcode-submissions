class Solution:

    def encode(self, strs: List[str]) -> str:
        print("input = ",strs )
        res = []
        for s in strs:
            len_s = len(s)
            res.append(str(len_s) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        # 2 ab
        # 1 c
        # 2#ab10#abcdefghij
        # 01234567        16

        def getLength(s, i):
            j = i
            while s[j] != "#":
                j += 1
            return s[i:j], j

        print("in s = ", s)
        res = []

        i = 0
        while i < len(s):
            num_chr, num_end_idx = getLength(s, i)
            st = num_end_idx + 1 #1
            ed = st + int(num_chr) #1+2 = 3
            decoded = s[st:ed]
            res.append(decoded)
            i = ed

        return res
