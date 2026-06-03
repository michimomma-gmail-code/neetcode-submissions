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
            mem = ""
            while stack and stack[-1] != "[":
                mem = stack.pop() + mem
            stack.pop() # remove "["
            num = ""
            while stack and "0" <= (stack[-1]) <= "9":
                num = stack.pop() + num
#            print(mem, num)
            stack.append(mem * int(num))

        return "".join(stack)
