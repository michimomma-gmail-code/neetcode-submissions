class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        temp = []

        if not digits:
            return []

        map = {"1": []
                , "2": ["A","B","c"]
                , "3": ["D", "E", "F"]
                , "4": ["G", "H", "I"]
                , "5": ["J", "K", "L"]
                , "6": ["M", "N", "O"]
                , "7": ["P", "Q", "R", "S"]
                , "8": ["T", "U", "V"]
                , "9": ["W", "X", "Y", "Z"]
                , "0": ["+"]
        }

        def dfs(i, substring):
            if len(substring) == len(digits):
                result.append(substring)
                return
            if i >= len(digits):
                return
            
            tails = map[digits[i]]
            for t in tails:
                t = t.lower()
#                temp.append(substring + t)
                dfs(i + 1, substring + t)
            
        dfs(0, "")

        return result

