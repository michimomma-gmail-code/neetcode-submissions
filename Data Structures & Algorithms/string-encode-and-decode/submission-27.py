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








    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            sls = str(len(s))
            res.append(str(len(sls)))
            res.append(sls)
            res.append(s)

        print(res)
        return "".join(res)



    def decode(self, s: str) -> List[str]:
        print(s)

        i = 0
        res = []
        while i < len(s):
            len_len = int(s[i])
            len_s = int(s[(i + 1) : (i + 1 + len_len)])
#            print(len_s)
            st = i + 1 + len_len
#            print( s[ st : st + len_s ] )
            res.append(s[ st : st + len_s ])
            i = st + len_s
#        print(res)
        return res
































