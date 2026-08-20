class Solution:

    def encode_(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            ls = str(len(s))
#            print(f"{len(ls)}, {ls}, {s}")
            out.append(str(len(ls)))
            out.append(ls)
            out.append(s)
#        print(out)
        return "".join(out)

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            ls = str(len(s))
            out.append(ls + "#" + s)
#        print(out)
        return "".join(out)


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
#        print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            len_word = int(s[i : j])
            j += 1
            word = s[j : j + len_word ]
#            print(word)
            res.append(word)
            i = j + len_word                
#        print(res)
        return res