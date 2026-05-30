class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt1, pt2 = 0, 0

        res = []
        count = 0
        while pt1 < len(word1) and pt2 < len(word2):
            
            if count % 2 == 0:
                res.append(word1[pt1])
                pt1 += 1
            else:
                res.append(word2[pt2])
                pt2 += 1

            count += 1


        if pt1 < len(word1):
            res.append(word1[pt1:])
        else:
            res.append(word2[pt2:])

        return "".join(res)