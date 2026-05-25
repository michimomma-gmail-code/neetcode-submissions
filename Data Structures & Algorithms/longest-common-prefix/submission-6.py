class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        reference = strs[0]

        j = 0
        index = 0
        while j < len(reference):
            res = True
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != reference[j]:
                    res = False
                    break
            if not res:
                break
            j += 1
        
        return reference[: j]        
