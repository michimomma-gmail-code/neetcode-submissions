class Solution:
    def decodeString(self, s: str) -> str:
        # 2[a3[b]]c
        # 2 push : 2
        # [ push: 2[
        # a push: 2[a
        # 3 push: 2[a3
        # [ push: 2[a3[
        # b push: 2[a3[b
        # ] pop (until find [): 2[a3 -> save b
        # pop once more : 3 : 2[a
        # generate b * 3 = bbb -> push: 2[abbb
        # ] pop (until find [): 2 -> save abbb
        # pop once more: 2: []
        # generate abbb * 2, push [abbbabbb]
        # c push. [abbbabbbc]

        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
                continue
            substring = []
            while stack and stack[-1] != "[":
            #    mem = stack.pop() + mem
                substring.append( stack.pop() )
            stack.pop() # remove "["
            num = []
            while stack and stack[-1].isdigit():
                num.append(stack.pop())
#            print(mem, num)
            substring = "".join(substring[::-1])
            num = "".join(num[::-1])
            stack.append(substring * int(num))

        return "".join(stack)
