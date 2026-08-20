class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            ls = str(len(s))
#            print(f"{len(ls)}, {ls}, {s}")
            out.append(str(len(ls)))
            out.append(ls)
            out.append(s)
#        print(out)
        return "".join(out)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
#        print(s)
        while i < len(s):
            char = s[i]
            len_len = int(char)
            len_word = int(s[i + 1: i + 1 + len_len])
#            print(len_len, len_word)
            word = s[i + 1 + len_len : i + len_len + len_word + 1]
#            print(word)
            res.append(word)
            i = i + len_len + len_word + 1
                
#        print(res)
        return res