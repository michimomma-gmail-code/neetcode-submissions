class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
#        plist = ["[]", "()", "{}"]
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