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



    def isValid(self, s: str) -> bool:
        stack = []

        right2left = {")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in ("(", "{", "["):
                stack.append(char)
            if char in right2left:
                if stack and stack[-1] != right2left[char]:
                    return False
                elif not stack:
                    return False                    
                else:
                    stack.pop()
        print('stack = ', stack)
        if stack:
            return False
        return True




























