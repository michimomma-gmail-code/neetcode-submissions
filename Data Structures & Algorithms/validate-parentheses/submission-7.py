class Solution:
    def isValid0(self, s: str) -> bool:
        stack = []
        cl = {
            "]" : "["
            , ")" : "("
            , "}" : "{"
            }


        for i in range(len(s)):
            if s[i] in ("[", "(", "{"):
                stack.append(s[i])
            elif s[i] in ("]", ")","}"):
                if len(stack) == 0:
                    return False
                if stack[-1] == cl[s[i]]:
                    stack.pop()
                else:
                    return False

        if len(stack):
            return False
        return True

    def isValid(self, s: str) -> bool:
        stack = []
        cl = {
            "]" : "["
            , ")" : "("
            , "}" : "{"
            }

        for c in s:
            if c in cl:
                if stack and stack[-1] == cl[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
