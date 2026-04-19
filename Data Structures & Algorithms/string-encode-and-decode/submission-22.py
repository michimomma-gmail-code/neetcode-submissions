class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))+"#"+s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        print("instring = ", s)
        # 1#a3#abc
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            str_len = int(s[i:j])
            st = j+1
            ed = st + str_len
            res.append(s[st:ed])
            print(str_len, s[st:ed])
            i = ed
        return res
